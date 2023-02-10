from flask import Blueprint
from flask_restx import Resource, Api, fields


bp = Blueprint('hashtag', __name__, url_prefix='/hashtag')
api = Api(bp)


@api.route('/')  # post
class CreateHashtag(Resource):
    def post(self):
        pass


@api.route('/<int:size>/<int:page>')
class GetHashtagByFilter(Resource):
    def get(self, size: int = 20, page: int = 1):
        pass


@api.route('/<string:hashtag_name>')  # get
class GetHashtagByName(Resource):
    def get(self, hashtag_name: str):
        pass
