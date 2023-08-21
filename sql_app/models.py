from sqlalchemy import Integer, String, ForeignKey, Column, DateTime

from sql_app.database import Base


class Estagiarios(Base):
    __tablename__ = 'estagiarios'

    id = Column(Integer, primary_key=True)
    nome = Column(String, nullable=True)
    curso = Column(String, nullable=True)
    semestre = Column(String, nullable=True)
    matricula = Column(String, nullable=True)



class Imagens(Base):
    __tablename__ = 'imagens'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    id_user = Column(Integer, ForeignKey("estagiarios.id"))
    path_imagem = Column(String)


class Logs(Base):
    __tablename__ = 'logs'

    id = Column(Integer, primary_key=True, autoincrement=True)
    id_user = Column(Integer, ForeignKey("estagiarios.id"))
    data_entrada = Column(DateTime)
    data_saida = Column(DateTime)
