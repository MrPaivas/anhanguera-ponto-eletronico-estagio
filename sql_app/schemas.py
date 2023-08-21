from pydantic import BaseModel
from typing import Optional

class EstagiariosBase(BaseModel):
    matricula: str
    nome: str
    curso: str
    semestre: str




class EstagiariosCreate(EstagiariosBase):
    pass

class Estagiarios(EstagiariosBase):
    id: int

    class Config:
        from_attributes = True


class ImagensBase(BaseModel):
    path_imagem: str | None = None


class ImagensCreate(ImagensBase):
    id_user: int | None = None


class Imagens(ImagensBase):
    id: int | None = None

    class Config:
        from_attributes = True


class LogsBase(BaseModel):
    data_entrada: str | None = None
    data_saida: str | None = None


class LogsCreate(LogsBase):
    id_user: int


class Logs(LogsBase):
    id: int
    
    class Config:
        from_attributes = True