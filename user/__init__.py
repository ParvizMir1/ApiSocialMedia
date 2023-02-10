from flask import Blueprint
from flask_restx import Resource, Api, fields

bp = Blueprint('users', __name__, url_prefix='/user')

# Регистрируем как swargger
api = Api(bp)


@api.route('/')  # get/post
class GetAllUsersOrCreateUser(Resource):
    def get(self):
        pass

    def post(self):
        pass


@api.route('/<int:user_id>')  # get
class GetExactUser(Resource):
    def get(self, user_id: int):
        pass


@api.route('/<int:photo_id>')  # put/delete
class ChangeUserPhotoOrDelete(Resource):
    def put(self, photo_id: int):
        pass

    def delete(self, photo_id: int):
        pass
