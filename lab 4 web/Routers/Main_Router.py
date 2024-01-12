from fastapi.responses import JSONResponse
from fastapi import APIRouter, Depends
from Database.database_creator import *
from Database.Schemas.Schemas import  *
from Models.Models import UserCreate

# создание таблиц
Base.metadata.create_all(bind=engine)
#создание маршрутизатора для обработки путей
router = APIRouter()

# Get запрос
@router.get("/todo")
def get_todo_user_id():
    db = SessionLocal()
    res = db.query(ToDo).all()
    db.close()
    return res

#добавление
@router.post("/user")
def add_user(data: UserCreate):
    db = SessionLocal()

    user = ToDo(name=data.name, task=data.task)
    db.add(user)
    db.commit()

    db.close()
    return data

#изменение пользователя и его задач
@router.put("/todo/{user_id}")
def update_todo_user_id(user_id: int, data: UserCreate):
    db = SessionLocal()

    user = db.query(ToDo).filter(ToDo.id == user_id).first()
    if user == None:
        return JSONResponse(status_code=404, content={"message": "Пользователь не найден"})

    user.task = data.task
    db.commit()

    db.close()
    return {"message": "Все изменения сохранены!"}

#удаление пользолвателя
@router.delete("/todo/{user_id}")
def delete_todo_user_id(user_id: int):
    db = SessionLocal()

    user = db.query(ToDo).filter(ToDo.id == user_id).first()
    if user == None:
        return JSONResponse(status_code=404, content={"message": "Пользователь не найден"})

    db.delete(user)
    db.commit()

    db.close()
    return {"message": "Пользователь был успешно удален"}