from flask import Blueprint, request
from flask_restx import Resource, Api, fields
from database.models import Comment
from datetime import datetime

bp = Blueprint('comments', __name__, url_prefix='/comments')
api = Api(bp)

comment_model = api.model('comment_model', {'comment_text': fields.String})


# Получение комментария
@api.route('/<int:post_id>')  # get/post
class GetOrPostComment(Resource):
    def get(self, post_id: int):
        current_comment = Comment.query.get_or_404(post_id)
        if current_comment:
            result = {'id': current_comment.id,
                      'main_text': current_comment.text,
                      'post_id': current_comment.post_id,
                      'post_likes': current_comment.likes,
                      'publish_date': str(current_comment.publish_date)
                      }

            return {'status': 1, 'message': result}

        return {'status': 0, 'message': 'Коментов пока нет'}

    # Добавление комментария
    @api.expect(comment_model)
    def post(self, post_id: int):
        print(post_id)
        response = request.json
        comment_text = response.get('comment_text')
        publish_date = datetime.now()

        try:
            Comment().add_comment(comment_text, post_id, publish_date)

            return {'status': 1, 'message': 'Успешно добавлено'}

        except Exception as e:
            print(e)
            return {'status': 0, 'message': 'Ошибка в данных'}


# Изменение текста комментария
@api.route('/<int:comment_id>/<string:new_comment_text>')
class ChangeComment(Resource):
    def put(self, comment_id: int, new_comment_text: str):
        try:
            Comment().change_text(comment_id, new_comment_text)

            return {'status': 1, 'message': 'Успешно обновлено'}

        except Exception as e:
            print(e)
            return {'status': 0, 'message': 'Ошибка в данных'}


# Добавить лайк к комментарии
@api.route('/<int:liked_comment_id>')
class AddLikeToComment(Resource):
    def put(self, liked_comment_id):
        try:
            Comment().likes_detect(liked_comment_id)

            return {'status': 1, 'message': 'Успешно +1 лайк'}

        except Exception as e:
            print(e)
            return {'status': 0, 'message': 'Ошибка в данных'}


# Удаление комментария
@api.route('/<int:comment_id>')
class DeleteComment(Resource):
    def delete(self, comment_id: int):
        try:
            Comment().delete_comment(comment_id)

            return {'status': 1, 'message': 'Успешно удален'}

        except Exception as e:
            print(e)
            return {'status': 0, 'message': 'Ошибка в данных'}
