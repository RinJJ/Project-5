from flask import Flask, request, make_response, session
from flask_bcrypt import Bcrypt
from flask_migrate import Migrate
from flask_restful import Api, Resource
from config import app, db, api, bcrypt
from models import *


#TODO: remember that we need seperate gets that get get a list of Groups by User/Username and by Character
#TODO: how to differentiate the User ID in Groups from the User id's related to the characters. Does it even matter due to scope?
#TODO:



app.secret_key = b'\x0e8.\xe0[\xdf\x01\x06\xc3\x8e\xf3\xeb\xdb\x0c\x7f\x88'

class Home(Resource):
    def get(self):
        return make_response("server is connected", 200)

api.add_resource(Home, '/')







class User(Resource):
    def get(self):
        users = User.query.all()
        if users == None:
            return make_response( { 'error' : '404: Users Not Found' } )
        users_dict = [user.to_dict() for user in users]
        return make_response( users_dict, 200 )

    def post(self):
        try:
            data = request.get_json()
            new_user = User(
                username = data['username'],
                email = data['email'],
                password = data['password'],
            )
            db.session.add( new_user )
            db.session.commit()
            session['user_id'] = new_user.user_id  ### if it doesnt work check ix auth video #1 @17:00 user_id is what i called id in models
            new_user_dict = new_user.to_dict()
            return make_response(new_user_dict, 201)
        except Exception as e:
            db.session.rollback()
            return make_response( { 'Error' : str(e) }, 422 )

api.add_resource(User, '/users')







class UserById(Resource):
    def get(self, id):
        user_by_id = User.query.filter(User.id == id).first()
        if user_by_id == None:
            return make_response( { 'error' : '404 User not found' } )
        user_by_id_dict = user_by_id.to_dict()
        return make_response( user_by_id_dict, 200 )

    def patch(self, id):
        try:
            user_by_id = User.query.filter(User.id == id).first()
            if user_by_id == None:
                return make_response( { 'error' : '404 User not found' } ) 
            for attr in request.get_json():
                setattr( user_by_id, attr, request.get_json()[attr] )
            db.session.add( user_by_id )
            db.session.commit()
            user_by_id_dict = user_by_id.to_dict()
            return make_response(user_by_id_dict, 201 )
        except Exception as e:
            db.session.rollback()
            return make_response( { "error" : str(e) }, 422 )
        
    def delete(self,id):
        try:
            user_by_id = User.query.filter(User.id == id).first()
            if user_by_id == None:
                return make_response( { 'error' : '404 User not found' } ) 
            db.session.delete(user_by_id)
            db.session.commit()
            return make_response( {} )
        except Exception as e:
            db.session.rollback()
            return make_response( { "error" : str(e) }, 422 )

api.add_resource(UserById, '/users/<int:id>')







class Character(Resource):
    def get(self):
        characters = Character.query.all()
        if characters == None:
            return make_response( { 'error' : '404: Characters Not Found' } )
        characters_dict = [character.to_dict() for character in characters]
        return make_response( characters_dict, 200 )

    def post(self):
        try:
            data = request.get_json()
            new_character = Character(
                character_name = data['character_name'],
                character_race = data['character_race'],
                character_class = data['character_class'],
            )
            db.session.add( new_character )
            db.session.commit()
            new_character_dict = new_character.to_dict()
            return make_response(new_character_dict, 200)
        except Exception as e:
            db.session.rollback()
            return make_response( { 'Error' : str(e) }, 422 )

api.add_resource(Character, '/characters')







class CharacterById(Resource):
    def get(self, id):
        character_by_id = Character.query.filter(Character.id == id).first()
        if character_by_id == None:
            return make_response( { 'error' : '404 Character not found' } )
        character_by_id_dict = character_by_id.to_dict()
        return make_response( character_by_id_dict, 200 )

    def patch(self, id):
        try:
            character_by_id = Character.query.filter(Character.id == id).first()
            if character_by_id == None:
                return make_response( { 'error' : '404 Character not found' } ) 
            for attr in request.get_json():
                setattr( character_by_id, attr, request.get_json()[attr] )
            db.session.add( character_by_id )
            db.session.commit()
            character_by_id_dict = character_by_id.to_dict()
            return make_response(character_by_id_dict, 201 )
        except Exception as e:
            db.session.rollback()
            return make_response( { "error" : str(e) }, 422 )
        
    def delete(self,id):
        try:
            character_by_id = Character.query.filter(Character.id == id).first()
            if character_by_id == None:
                return make_response( { 'error' : '404 Character not found' } ) 
            db.session.delete(character_by_id)
            db.session.commit()
            return make_response( {} )
        except Exception as e:
            db.session.rollback()
            return make_response( { "error" : str(e) }, 422 )

api.add_resource(CharacterById, '/characters/<int:id>')







class Group(Resource):
    def get(self):
        groups = Group.query.all()
        if groups == None:
            return make_response( { 'error' : '404: Groups Not Found' } )
        groups_dict = [group.to_dict() for group in groups]
        return make_response( groups_dict, 200 )

    def post(self):
        try:
            data = request.get_json()
            new_group = Group(
                group_name = data['group_name'],
                user_id = data['user_id'], ### we wnat to snag the username from this?
            )
            db.session.add( new_group )
            db.session.commit()
            new_group_dict = new_group.to_dict()
            return make_response(new_group_dict, 200)
        except Exception as e:
            db.session.rollback()
            return make_response( { 'Error' : str(e) }, 422 )

api.add_resource(Group, '/groups/')







class GroupById(Resource):
    def get(self, id):
        group_by_id = Group.query.filter(Group.id == id).first()
        if group_by_id == None:
            return make_response( { 'error' : '404 Group not found' } )
        group_by_id_dict = group_by_id.to_dict()
        return make_response( group_by_id_dict, 200 )

    def patch(self, id):
        try:
            group_by_id = Group.query.filter(Group.id == id).first()
            if group_by_id == None:
                return make_response( { 'error' : '404 Group not found' } ) 
            for attr in request.get_json():
                setattr( group_by_id, attr, request.get_json()[attr] )
            db.session.add( group_by_id )
            db.session.commit()
            group_by_id_dict = group_by_id.to_dict()
            return make_response(group_by_id_dict, 201 )
        except Exception as e:
            db.session.rollback()
            return make_response( { "error" : str(e) }, 422 )
        
    def delete(self,id):
        try:
            group_by_id = Group.query.filter(Group.id == id).first()
            if group_by_id == None:
                return make_response( { 'error' : '404 Group not found' } ) 
            db.session.delete(group_by_id)
            db.session.commit()
            return make_response( {} )
        except Exception as e:
            db.session.rollback()
            return make_response( { "error" : str(e) }, 422 )

api.add_resource(GroupById, '/groups/<int:id>')







class CharacterGroup(Resource):
    def get(self):
        character_groups = CharacterGroup.query.all()
        if character_groups == None:
            return make_response( { 'error' : '404: CharacterGroups Not Found' } )
        character_groups_dict = [character_group.to_dict() for character_group in character_groups]
        return make_response( character_groups_dict, 200 )

    def post(self):
        try:
            data = request.get_json()
            new_character_group = CharacterGroup(
                character_id = data['character_id'],
                group_id = data['group_id'],
            )
            db.session.add( new_character_group )
            db.session.commit()
            new_character_group_dict = new_character_group.to_dict()
            return make_response(new_character_group_dict, 200)
        except Exception as e:
            db.session.rollback()
            return make_response( { 'Error' : str(e) }, 422 )

api.add_resource(CharacterGroup, '/CharacterGroups/')







class CharacterGroupById(Resource):
    def get(self, id):
        character_group_by_id = CharacterGroupById.query.filter(CharacterGroupById.id == id).first()
        if character_group_by_id == None:
            return make_response( { 'error' : '404 CharacterGroupee not found' } )
        character_group_by_id_dict = character_group_by_id.to_dict()
        return make_response( character_group_by_id_dict, 200 )

    def patch(self, id):
        try:
            group_by_id = Group.query.filter(Group.id == id).first()
            if group_by_id == None:
                return make_response( { 'error' : '404 Group not found' } ) 
            for attr in request.get_json():
                setattr( group_by_id, attr, request.get_json()[attr] )
            db.session.add( group_by_id )
            db.session.commit()
            group_by_id_dict = group_by_id.to_dict()
            return make_response(group_by_id_dict, 201 )
        except Exception as e:
            db.session.rollback()
            return make_response( { "error" : str(e) }, 422 )
        
    def delete(self,id):
        try:
            group_by_id = Group.query.filter(Group.id == id).first()
            if group_by_id == None:
                return make_response( { 'error' : '404 Group not found' } ) 
            db.session.delete(group_by_id)
            db.session.commit()
            return make_response( {} )
        except Exception as e:
            db.session.rollback()
            return make_response( { "error" : str(e) }, 422 )

api.add_resource(CharacterGroupById, '/CharacterGroups/<int:id>')

class Login(Resource):
    def post(self):
        try:
            user = User.query.filter_by(user_id=request.get_json()['user_id']).first()
            session['user_id'] = user.user_id  ###named this way due to how the tables are setup?
            response = make_response(user.to_dict(), 200)
            return response
        except:  ### here we need to ad the password validations
            pass

api.add_resource(Login, '/Login')

class Logout(Resource):
    def delete(self):
        session['user_id'] = None
        response = make_response('',204)
        return response

api.add_resource(Logout, '/Logout')

class AuthorizedSession(Resource):
    def get(self):
        user = User.query.filter_by(user_id=session.get('user_id')).first()
        if user:
            response = make_response(
                user.to_dict(), 200
            )
            return response
        else:
            return make_response( { 'Unauthorized': 401 } )

api.add_resource(AuthorizedSession, 'authorized')









# class CharacterGroupByUser(Resource):
#     def get(self, id):
#         pass

# class CharacterGroupByCharacter(Resource):
#     def get(self, id):
#         pass


# Do we need the two above



































if __name__ == '__main__':
    app.run(port=5555, debug=True)