from core.configs import settings
from sqlalchemy import Column, Integer, String

#DBBaseModel é a classe declarativa do SQLAlchemy

class CursoModel(settings.DBBaseModel):
    __tablename__ = "cursos"
    id: int = Column(Integer, primary_key=True, autoincrement=True)
    titulo: str = Column(String(100))
    horas: int = Column(Integer)
    aulas: int = Column(Integer)
    instrutor: str = Column(String(100))