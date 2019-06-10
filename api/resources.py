from flask_restful import Resource, reqparse

from api.models import UserModel

parser = reqparse.RequestParser()
parser.add_argument('username', help = 'This field cannot be blank', required= True)
parser.add_argument('password', help = 'This field cannot be blank', required= True)



class UserRegistration(Resource):
    def post(self):
        data = parser.parse_args()

        if UserModel.find_by_username(data['username']):
            return {
                'message': f"{data['username']} already exists!!"
            }, 400

        new_user = UserModel(
            username=data['username'],
            password=data['password']
        )
        try:
            new_user.save_to_db()
            return {
                'message': f"User {data['username']} was created."
            }, 201
        except:
            return {
                'message': 'Something went wrong'}, 500


class UserLogin(Resource):
    def post(self):
        data = parser.parse_args()

        current_user = UserModel.find_by_username(data['username'])

        if not current_user:
            return {
                'message' : f"User {data['username']} doesn\'t exist"
            }, 400

        if data['password'] == current_user.password:
            return {
                'message': f'Logged in as {current_user.username}'
            }, 200
        else:
            return {
                'message': 'Wrong credentials'
            }, 400


class UserLogoutAccess(Resource):
    def post(self):
        return {'message': 'User logout'}


class UserLogoutRefresh(Resource):
    def post(self):
        return {'message': 'User logout'}


class TokenRefresh(Resource):
    def post(self):
        return {'message': 'Token refresh'}


class AllUsers(Resource):
    def get(self):
        return UserModel.return_all()

    def delete(self):
        return UserModel.delete_all()


class SecretResource(Resource):
    def get(self):
        return {
            'answer': 42
        }