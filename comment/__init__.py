from flask import Blueprint
from flask_restx import Resource, Api, fields


bp = Blueprint('comments', __name__, url_prefix='/comment')
api = Api(bp)


@api.route('/<int:exact_post_id>')  # get/post
class GetOrPostCommentByPostId(Resource):
    def get(self, exact_post_id: int):
        pass

    def post(self, exact_post_id: int):
        pass


@api.route('/<int:post_id>')  # put/delete
class ChangeOrDeleteCommentByPostId(Resource):
    def put(self, post_id: int):
        pass

    def delete(self, post_id: int):
        pass
