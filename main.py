from fastapi import FastAPI, HTTPException, status, Depends
from pydantic import BaseModel
from sqlalchemy.orm import Session
from models import TodoInDB
from database import SessionLocal, init_db

app = FastAPI()

@app.on_event("startup")
async def startup():
    init_db()

class Todo(BaseModel):
    task: str
    completed: bool

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def to_dict(obj):
    return {
        column.name: getattr(obj, column.name) for column in obj.__table__.columns
    }

@app.get("/todos", response_model=list[dict])
def read_todos(db: Session = Depends(get_db)):
    todos = db.query(TodoInDB).all()
    return [to_dict(todo) for todo in todos]

@app.post("/todos", response_model=dict, status_code=status.HTTP_201_CREATED)
def create_todo(todo: Todo, db: Session = Depends(get_db)):
    db_todo = TodoInDB(**todo.model_dump())
    db.add(db_todo)
    db.commit()
    db.refresh(db_todo)
    return to_dict(db_todo)

@app.put("/todos/{todo_id}", response_model=dict)
def update_todo(todo_id: int, todo: Todo, db: Session = Depends(get_db)):
    db_todo = db.query(TodoInDB).filter(TodoInDB.id == todo_id).first()
    if db_todo is None:
        raise HTTPException(status_code=404, detail="Todo not found")
    for key, value in todo.model_dump().items():
        setattr(db_todo, key, value)
    db.commit()
    db.refresh(db_todo)
    return to_dict(db_todo)

@app.delete("/todos/{todo_id}", response_model=dict)
def delete_todo(todo_id: int, db: Session = Depends(get_db)):
    db_todo = db.query(TodoInDB).filter(TodoInDB.id == todo_id).first()
    if db_todo is None:
        raise HTTPException(status_code=404, detail="Todo not found")
    db.delete(db_todo)
    db.commit()
    return {"message": "Todo deleted successfully"}
