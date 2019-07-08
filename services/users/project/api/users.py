# services/users/project/api/users.py


from flask import Blueprint, request
from flask_restful import Resource, Api
from project.api.models import User
from project.db import database
from flask_mongoengine import ValidationError


users_blueprint = Blueprint('users', __name__)
api = Api(users_blueprint)


class UsersPing(Resource):
    def get(self):
        return {
            'status': 'success',
            'message': 'pong!'
        }


class UsersList(Resource):
    def get(self):
        """Get all users"""
        db = database.get_mongoDB()
        cursor = db.user.find()
        users = []
        for item in cursor:
            users.extend([item["username"], item["email"], item["active"]])

        response_object = {
            'status': 'success',
            'data': {
                'users': users
            }
        }
        return response_object, 200

    def post(self):
        post_data = request.get_json()
        response_object = {
            'status': 'fail',
            'message': 'Invalid payload.'
        }
        if not post_data:
            return response_object, 400

        username = post_data.get('username')
        email = post_data.get('email')

        try:
            # open connection to the database
            db = database.get_mongoDB()
            user = db.user.find_one({"email": email})
            if not user:
                newUser = User(username=username, email=email)
                newUser.save()

                response_object = {
                    'status': 'success',
                    'message': f'{email} was added!'
                }
                return response_object, 200

            else:
                response_object['message'] = 'Sorry. That email already exists.'
                return response_object, 400

        except ValidationError:
            # if the write fails, OperationalError is thrown
            return response_object, 400


class Users(Resource):
    def get(self, username):
        """Get single user details"""
        response_object = {
            'status': 'fail',
            'message': 'User does not exist'
        }

        db = database.get_mongoDB()
        try:
            dude = db.user.find_one({"username": username})
            if not dude:
                return response_object, 404
            else:
                response_object = {
                    'status': 'success',
                    'data': {
                        'id': str(dude["_id"]),
                        'username': dude["username"],
                        'email': dude["email"],
                        'active': dude["active"]
                    }
                }
                return response_object, 200

        except ValueError:
            return response_object, 404


api.add_resource(UsersPing, '/users/ping')
api.add_resource(UsersList, '/users')
api.add_resource(Users, '/users/<username>')
