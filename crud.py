from sqlalchemy.orm import Session
from model import Item


def list_items(db):
    return db.query(Item).all()


def get_item(db, item_id):
    return db.query(Item).filter(Item.id == item_id).first()


def create_item(db, title, description):
    item = Item(title=title, description=description)
    db.add(item)
    db.commit()
    db.refresh(item)
    return item


def update_item(db, item, title=None, description=None):
    if title is not None:
        item.title = title
    if description is not None:
        item.description = description
    db.commit()
    db.refresh(item)
    return item


def delete_item(db, item):
    db.delete(item)
    db.commit()

