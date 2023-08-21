from sqlalchemy.orm import Session


from sql_app.database import SessionLocal
from sql_app import models
from sql_app import schemas

def get_users(db: Session):
    return db.query(models.Estagiarios).all()


def get_user_by_matricula(db: Session, matricula: str):
    busca = db.query(models.Estagiarios).filter(models.Estagiarios.matricula == matricula).first()
    return busca


def get_users_by_curso(db: Session, curso: str):
    busca = db.query(models.Estagiarios).filter(models.Estagiarios.curso == curso).all()
    return busca


def get_users_by_semestre(db: Session, semestre: str):
    busca = db.query(models.Estagiarios).filter(models.Estagiarios.semestre == semestre).all()
    return busca


def get_user_image_by_matricula(db: Session, matricula: str):
    busca_id = db.query(models.Estagiarios).filter(models.Estagiarios.matricula == matricula).first()
    busca_imagem = db.query(models.Imagens).filter(models.Imagens.id == busca_id.id).first()
    return busca_imagem



def get_log_by_matricula(db: Session, matricula: str):
    busca_id = db.query(models.Estagiarios).filter(models.Estagiarios.matricula == matricula).first()
    busca = db.query(models.Logs).filter(models.Logs.id_user == busca_id.id).all()
    return busca


def create_user(db: Session, user: schemas.EstagiariosCreate):  
    db_user = models.Estagiarios(
        nome = user.nome,
        curso = user.curso,
        semestre = user.semestre,
        matricula = user.matricula
        )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def save_image(db: Session, img: schemas.ImagensCreate):
    db_image = models.Imagens(
        id_user = img.id_user,
        path_imagem = img.path_imagem
    )
    db.add(db_image)
    db.commit()
    db.refresh(db_image)
    return db_image


def create_log_entrada_by_matricula(db: Session, log: schemas.LogsCreate):
    loging = models.Logs(
        id_user = int(log.id_user),
        data_entrada = log.data_entrada
    )
    db.add(loging)
    db.commit()
    db.refresh(loging)
    return loging


def create_log_saida_by_matricula(db: Session, matricula:str, data_saida: str):
    busca_id = db.query(models.Estagiarios).filter(models.Estagiarios.matricula == matricula).first()
    busca_log = db.query(models.Logs).filter(models.Logs.id_user == busca_id.id).first()
    busca_log.data_saida = data_saida
    db.commit()
    db.refresh(busca_log)
    return busca_log
