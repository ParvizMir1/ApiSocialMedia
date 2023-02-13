from flask import Blueprint, request
from flask_restx import Resource, Api, fields
from database.models import Hashtag


bp = Blueprint('hashtag', __name__, url_prefix='/hashtags')
api = Api(bp)

hashtag_model = api.model('create_hashtag', {'post_id': fields.Integer,
                                             'hash_name': fields.String,
                                             })


@api.route('/hashtag')  # post/get
class CreateHashtag(Resource):
    def get(self, size: int = 20, page: int = 1):
        all_hashtags = Hashtag.query.limit(size).all()
        print(all_hashtags)
        if all_hashtags:
            result = [{i.post_id: i.hash_name} for i in all_hashtags]

            return {'status': 1, 'hashtags': result}

        return {'status': 0, 'hashtags': []}

    @api.expect(hashtag_model)
    def post(self):
        response = request.json
        post_id = response.get('post_id')
        hash_name = response.get('hash_name')

        try:
            Hashtag().add_hashtag(hash_name, post_id)
            return {'status': 1, 'message': 'Успешно добавлено'}

        except:
            return {'status': 0, 'message': 'Ошибка в данных'}


@api.route('/<string:hashtag_name>')  # get by hashtag name
class GetHashtagByName(Resource):
    def get(self, hashtag_name: str):
        current_hashtag = Hashtag.query.filter_by(hash_name=hashtag_name).first()
        print(current_hashtag.hash_name)

        if current_hashtag:
            return {'status': 1, 'hashtag_id': current_hashtag.id,
                    'current_hashtag': current_hashtag.hash_name, 'post_id': current_hashtag.post_id}

        return {'status': 0, 'message': 'Нету такого'}
