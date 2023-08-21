from pydantic import BaseModel, ValidationError
from fastapi import UploadFile, Form
from typing import Optional


class NewUserResponse(BaseModel):
    matricula: str = Form(...)
    nome: str = Form(...)
    curso: str = Form(...)
    semestre: str = Form(...)
    imagem: UploadFile = Form(...)