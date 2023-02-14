from flask_restx import Api, Resource
from flask import Blueprint

from database.models import User, Password

bp = Blueprint('autohentication', __name__, url_prefix='/auth')
api = Api(bp)

# Для получения ID пользователя
user_reg_models = api.parser()
user_reg_models.add_argument('username', type=str, required=True)

# Для изменения пароля
user_password_model = api.parser()
user_password_model.add_argument('user_id', type=int, required=True)
user_password_model.add_argument('new_password', type=str, required=True)

# Для создания пароля
user_password = api.parser()
user_password.add_argument('user_id', type=int, required=True)
user_password.add_argument('password', type=str, required=True)


# Методы для входа
@api.route('/log')
class AuthUser(Resource):
    # Получение айди пользователя
    @api.expect(user_reg_models)
    def get(self):
        username = user_reg_models.parse_args()
        current_username = username.get('username')

        current_user = User.query.filter_by(username=current_username)
        if current_user:
            return {'status': 1, 'user_id': current_user[0].id}

        return {'status': 0, 'message': 'Ошибка в данных'}

    # Изменение пароля
    @api.expect(user_password_model)
    def put(self):
        args = user_password_model.parse_args()

        user_id = args.get('user_id')
        user_new_password = args.get('new_password')

        result = Password().change_password(user_id, user_new_password)

        return {'status': 1, 'message': result}

    @api.expect(user_password)
    # Создать пароль пользователя
    def post(self):
        args = user_password.parse_args()

        user_id = args.get('user_id')
        password = args.get('password')

        Password().set_password(password, user_id)

        return {'status': 1, 'message': 'Пароль успешно создан'}
