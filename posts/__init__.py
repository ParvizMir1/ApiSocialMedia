from flask import Blueprint, request
from flask_restx import Resource, Api, fields

from database.models import Post
from datetime import datetime

from werkzeug.datastructures import FileStorage  # Для файлов

from werkzeug.utils import secure_filename
import os

bp = Blueprint('posts', __name__, url_prefix='/posts')
api = Api(bp)

# Для работы с файлами
upload_parser = api.parser()
upload_parser.add_argument('file', location='files', type=FileStorage)

# Создаем модель для тестирования
upload_parser.add_argument('header', type=str)
upload_parser.add_argument('main_text', type=str)
upload_parser.add_argument('user_id', type=str)


# @api.expect(upload_parser)
@api.route('/post')  # get/post
class GetAllPostsOrCreate(Resource):
    def get(self):
        all_posts = Post.query.all()

        if all_posts:
            result = [{'post_id': i.id,
                       'header': i.header,
                       'main_text': i.main_text,
                       'user_id': i.user_id,
                       'publish_date': str(i.publish_date),
                       'post_likes': i.post_likes} for i in all_posts]

            return {'status': 1, 'message': result}

        return {'status': 0, 'message': 'Постов пока нет'}

    @api.expect(upload_parser)
    def post(self):
        response = upload_parser.parse_args()
        post_image = response.get('file')
        print(post_image)
        header = response.get('header')
        main_text = response.get('main_text')
        user_id = response.get('user_id')
        publish_date = datetime.now()

        try:
            file_name = secure_filename(post_image.filename)
            post_image.save(os.path.join('media/', file_name))
            Post().create_post(header, main_text, publish_date, user_id, post_image)

            return {'status': 1, 'message': 'Пост успешно добавлен'}

        except Exception as e:
            print('e')
            return {'status': 0, 'message': 'Ошибка в данных'}


@api.route('/<int:post_id>')  # get exact post or delete
class GetPostOrDelete(Resource):
    def get(self, post_id: int):
        current_post = Post.query.get_or_404(post_id)

        if current_post:
            result = {'post_id': current_post.id,
                       'header': current_post.header,
                       'main_text': current_post.main_text,
                       'user_id': current_post.user_id,
                       'publish_date': str(current_post.publish_date),
                       'post_likes': current_post.post_likes}

            return {'status': 1, 'message': result}

        return {'status': 0, 'message': 'Постов пока нет'}

    def delete(self, post_id: int):
        try:
            Post().delete_post(post_id)

            return {'status': 1, 'message': 'Успешно удалено'}

        except:
            return {'status': 0, 'message': 'Пост не найден'}


# Изменение заголовка
@api.route('/<int:post_id>/<string:new_header>')
class ChangePostHeader(Resource):
    def put(self, post_id: int, new_header: str):
        try:
            Post().change_header(post_id, new_header)

            return {'status': 1, 'message': 'Успешео обновлено'}

        except:
            return {'status': 0, 'message': 'Ошибка в данных'}


@api.route('/<int:post_id>/<string:new_main_text>')
class ChangePostMainText(Resource):
    def put(self, post_id: int, new_main_text: str):
        try:
            Post().change_main_text(post_id, new_main_text)

            return {'status': 1, 'message': 'Успешео обновлено'}

        except:
            return {'status': 0, 'message': 'Ошибка в данных'}


@api.route('/<int:liked_post_id>')
class AddLikeToPost(Resource):
    def put(self, liked_post_id: int):
        try:
            Post().likes_detect(liked_post_id)

            return {'status': 1, 'message': '+1 Лайк'}

        except:
            return {'status': 0, 'message': 'Ошибка в данных'}
