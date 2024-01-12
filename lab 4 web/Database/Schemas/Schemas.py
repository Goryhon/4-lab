from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
#создает базовый класс для описания таблиц
Base = declarative_base()
#класс описывающий таблицу ToDo()
class ToDo(Base):
    __tablename__ = 'задачи'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(80))
    task = Column(String(256))
