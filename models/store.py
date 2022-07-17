from db import db


class StoreModel(db.Model):
    __tablename__ ='stores'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    
    def __init__(self,name):
        self.name = name

    def json(self):
        return {"id":self.id,"name":self.name,"price":self.price}

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
