from flask import Flask, request, make_response, session
from flask_migrate import Migrate
from flask_restful import Api, Resource
from config import app, db, api
from models import *


#TODO: remember that we need seperate gets that get get a list of Groups by User/Username and by Character
#TODO: how to differentiate the User ID in Groups from the User id's related to the characters. Does it even matter due to scope?
#TODO:





class Home(Resource):
    def get(self):
        return make_response("API is running", 200)

api.add_resource(Home, '/')

class User(Resource):
    def get(self):
        users = User.query.all()
        users_dict = [user.to_dict() for user in users]
        if users == None:
            return make_response( { 'error' : '404: Users Not Found' } )
        return make_response( users_dict, 200 )

    def post(self):
        try:
            data = request.get_json()
            new_user = User(
                username = data['username'],
                password = data['password'],
            )
            db.session.add( new_user )
            db.session.commit()
            user_dict = new_user.to_dict()
            return make_response(user_dict, 200)
        except Exception as e:
            db.session.rollback()
            return make_response( { 'Error' : str(e) }, 422 )

api.add_resource(User, '/users')






class UserById(Resource):
    def get(self, id):
        pass

class Character(Resource):
    def get(self):
        pass

class CharacterById(Resource):
    def get(self, id):
        pass


class Group(Resource):
    def get(self):
        pass


class GroupById(Resource):
    def get(self, id):
        pass

class CharacterGroup(Resource):
    def get(self):
        pass


class CharacterGroupById(Resource):
    def get(self, id):
        pass

class CharacterGroupByUser(Resource):
    def get(self, id):
        pass

class CharacterGroupByCharacter(Resource):
    def get(self, id):
        pass




































if __name__ == '__main__':
    app.run(port=5555, debug=True)