from flask_restful import Resource, reqparse

from models.store import StoreModel 

class Store(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument("price",
    type=float,
    required=True,
    help="This field cannot be empty")
    
    parser.add_argument("store_id",
    type=float,
    required=True,
    help="Every item must have store id")

    # @jwt_required()
    def get(self, name):
        item = StoreModel.find_by_name(name)
        if item is not None:
            return item.json()
        return {"message": 'store not found'}

    def post(self, name):
        if StoreModel.find_by_name(name) is not None:
            return {"item": f"Item name {name} is already exits" },400
        
        data = Item.parser.parse_args()
        item = StoreModel(name ,data['price'],data['store_id'])
        
        item.save_to_db()
        return {"message": "store created successfully"}

    def delete(self, name):
        item = ItemModel.find_by_name(name)
        if item:
            item.delete_from_db()

        return {"message": f"store name {name} is deleted successfully"}

    def put(self, name):
        data = Item.parser.parse_args()

        item = ItemModel.find_by_name(name)
        # updated_item = StoreModel(name ,data["price"])

        if item is None:
            # updated_item.save_to_db()
            item = StoreModel(name ,data['price'],data['store_id'])
            # return {"message": "Item created successfully"}
        else:
            item.price = data['price']
            # updated_item.update()
            # return {"message": "Item Updated successfully"}
        item.save_to_db()
        return  item.json()

class StoreList(Resource):
    def get(self):
        # pass
        return {'items': [item.json() for item in  StoreModel.query.all()]}
        # return {"items ": list(map(lambda x: x.json(), StoreModel.query.all()))}
