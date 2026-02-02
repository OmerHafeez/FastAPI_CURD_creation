from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from database import engine, Base, get_db
from crud import list_items, get_item, create_item, update_item, delete_item

Base.metadata.create_all(bind=engine)
app = FastAPI()


@app.get("/items")
def items(db: Session = Depends(get_db)):
    return list_items(db)


@app.get("/items/{id}")
def item(id: int, db: Session = Depends(get_db)):
    return get_item(db, id)


@app.post("/items")
def add(title: str, description: str, db: Session = Depends(get_db)):
    return create_item(db, title, description)


@app.put("/items/{id}")
def update(id: int, title: str, description: str, db: Session = Depends(get_db)):
    item = get_item(db, id)
    return update_item(db, item, title, description)


@app.delete("/items/{id}")
def delete(id: int, db: Session = Depends(get_db)):
    item = get_item(db, id)
    delete_item(db, item)
    return "Item deleted"