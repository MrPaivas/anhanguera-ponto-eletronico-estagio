from fastapi import Depends, HTTPException, APIRouter, UploadFile, File
from sqlalchemy.orm import Session
import uuid
from typing import Annotated


from sql_app import schemas
import crud.crud
from libraries.make_tempdir import make_dir_estagiario
from sql_app.sql_session import get_db
from schemas.new_user_response import NewUserResponse


router = APIRouter()


@router.post("/novo-estagiario", response_model=schemas.Estagiarios)
async def cadastrar_estagiario(novo_estagiario: NewUserResponse = Depends(),  db: Session = Depends(get_db)):
    db_user = crud.crud.get_user_by_matricula(db, novo_estagiario.matricula)
    if db_user:
        raise HTTPException(status_code=400, detail="Matricula já cadastrada")

    dir_path = await make_dir_estagiario(novo_estagiario.matricula)
    new_user = crud.crud.create_user(db, novo_estagiario)
    
    foto_name = uuid.uuid3(uuid.NAMESPACE_DNS, novo_estagiario.matricula)
    file_path = f"{dir_path}/{foto_name}.jpg"
    
    foto_data = await novo_estagiario.imagem.read()

    with open(file_path, "wb") as file:
        file.write(foto_data)

    salva_img = {
        'path_imagem': str(file_path),
        'id_user': int(new_user.id)
    }
    crud.crud.save_image(db, schemas.ImagensCreate(**salva_img))
    return new_user



@router.get("/estagiarios")
def listar_estagiarios(db: Session = Depends(get_db)):
    return crud.crud.get_users(db)


@router.get("/estagiarios/{matricula}", response_model=schemas.Estagiarios)
def achar_estagiarios(matricula: str, db: Session = Depends(get_db)):
    db_user = crud.crud.get_user_by_matricula(db, matricula)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user