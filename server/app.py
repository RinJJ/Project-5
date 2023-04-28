from flask import Flask, request, make_response, session
from flask_migrate import Migrate
from flask_restful import Api, Resource
from config import app, db, api
from models import *

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


































if __name__ == '__main__':
    app.run(port=5555, debug=True)