from flask import Blueprint, request
from flask_restx import Resource, Api, fields
from database.models import User

bp = Blueprint('users', __name__, url_prefix='/users')

# Регистрируем как swargger
api = Api(bp)

# Модель регистрации на swargger
user_model = api.model('user_creation',
                       {'username': fields.String,
                        'first_name': fields.String,
                        'last_name': fields.String,
                        'email': fields.String,
                        'phone_number': fields.String,
                        'about': fields.String
                        })


@api.route('/user')  # get/post
class GetAllUsersOrCreateUser(Resource):
    def get(self):
        all_users = User.query.all()

        if all_users:
            result = [{i.id: i.username} for i in all_users]

            return {'status': 1, 'users': result}

        return []

    @api.expect(user_model)
    def post(self):
        response = request.json

        # Берем данные из форм
        username = response.get('username')
        first_name = response.get('first_name')
        last_name = response.get('last_name')
        email = response.get('email')
        phone_number = response.get('phone_number')
        about = response.get('about')

        try:
            User().register_user(username=username, first_name=first_name, last_name=last_name, email=email,
                                phone_number=phone_number, about=about)

            return {'status': 1, 'message': 'Пользователь успешно создан'}

        except:
            return {'status': 0, 'message': 'Такой номер уже существует'}


@api.route('/<int:user_id>')  # get
class GetExactUser(Resource):
    def get(self, user_id: int):
        current_user = User.query.get_or_404(user_id)

        if current_user:
            return {'status': 1, 'user': {'username': current_user.username,
                                          'first_name': current_user.first_name,
                                          'last_name': current_user.last_name,
                                          'email': current_user.email,
                                          'phone_number': current_user.phone_number,
                                          'about': current_user.about
                                          }}

        return {'status': 0, 'message': 'Пользователь не найден'}


@api.route('/<int:photo_id>')  # put/delete
class ChangeUserPhotoOrDelete(Resource):
    def put(self, photo_id: int):
        pass

    def delete(self, photo_id: int):
        pass
