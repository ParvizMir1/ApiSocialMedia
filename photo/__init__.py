from flask import Blueprint
from flask_restx import Resource, Api, fields


bp = Blueprint('photo', __name__, url_prefix='/photo')
api = Api(bp)


@api.route('/')  # get/post
class GetAllPhotosOrAddPhoto(Resource):
    def get(self):
        pass

    def post(self):
        pass


@api.route('/<int:exact_photo_id>')  # get exact photo
class GetExactPhotoById(Resource):
    def get(self, exact_photo_id: int):
        pass


@api.route('/<int:photo_id>')  # put/delete
class ChangeOrDeletePhoto(Resource):
    def put(self, photo_id: int):
        pass

    def delete(self, photo_id: int):
        pass
