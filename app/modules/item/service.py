from app.modules.item.model import Item
from app import db

def get_all_items():
    return [item.to_dict() for item in Item.query.all()]

def get_item_by_id(item_id):
    item = db.session.get(Item, item_id)
    return item.to_dict() if item else None

def create_item(data):
    new_item = Item(
        name=data.get('name'),
        phone=data.get('phone'),
        email=data.get('email')
    )
    db.session.add(new_item)
    db.session.commit()
    return new_item.to_dict()

def update_item(item_id, data):
    item = db.session.get(Item, item_id)
    if not item:
        return None
    item.name = data.get('name', item.name)
    item.phone = data.get('phone', item.phone)
    item.email = data.get('email', item.email)
    db.session.commit()
    return item.to_dict()

def delete_item(item_id):
    item = db.session.get(Item, item_id)
    if not item:
        return False
    db.session.delete(item)
    db.session.commit()
    return True
