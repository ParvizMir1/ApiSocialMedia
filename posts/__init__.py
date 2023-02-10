from flask import Blueprint
from flask_restx import Resource, Api, fields


bp = Blueprint('posts', __name__, url_prefix='/posts')
api = Api(bp)


@api.route('/')  # get/post
class GetAllPostsOrCreate(Resource):
    def get(self):
        pass

    def post(self):
        pass


@api.route('/<int:exact_post_id>')  # get exact
class GetExactPost(Resource):
    def get(self, exact_post_id: int):
        pass


@api.route('/<int:post_id>')  # put/delete
class ChangePostOrDelete(Resource):
    def put(self, post_id: int):
        pass

    def delete(self, post_id: int):
        pass
