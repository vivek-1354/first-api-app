from db import db

class ItemModel(db.Model):
    __tablename__ ='items'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    price = db.Column(db.Float(precision =2))
    store_id = db.Column(db.Integer ,db.Foreignkey('stores.id'))
    
    db.relationship(StoreModel)
    
    def __init__(self,name,price,store_id):
        self.name = name
        self.price = price
        self.store_id = store_id


    def json(self):
        return {"id":self.id,"name":self.name,"price":self.price,"store_id :self.store_id"}

        # This function authorization if item name exits in database data.sqlite if not exits return none
    @classmethod
    def find_by_name(cls,name):
        return cls.query.filter_by(name =name).first()
    
    def save_to_db(self):
        db.session.add(self)
        db.session.commit()
 
    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()





