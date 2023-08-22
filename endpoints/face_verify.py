from datetime import datetime
from fastapi import Depends, HTTPException, APIRouter, File, UploadFile
from sqlalchemy.orm import Session
import uuid


from face_finder.face_recognition import face_verify
from libraries.make_tempdir import make_dir_estagiario
from schemas.face_verify import FaceVerifyResponse
from sql_app import schemas
import crud.crud
from sql_app.sql_session import get_db



router = APIRouter()


@router.post("/verificacao-facial/{matricula}", response_model=FaceVerifyResponse)
async def verificacao_facial( matricula: str , db: Session = Depends(get_db), foto: UploadFile = File(...)):
    
    user = crud.crud.get_user_by_matricula(db, matricula)
    data_base_image = crud.crud.get_user_image_by_matricula(db, user.matricula)
    user_dir = await make_dir_estagiario(matricula)
    foto_name = uuid.uuid3(uuid.NAMESPACE_DNS, user.nome)
    file_path = f"{user_dir}/{foto_name}.jpg"
    
    foto_data = await foto.read()
    with open(file_path, "wb") as file:
        file.write(foto_data)
    
    return face_verify(data_base_image.path_imagem, file_path)


