from flask import Blueprint

bp = Blueprint('users', __name__, url_prefix='/user')


@bp.get('/')
def get_all_users():
    pass


@bp.post('/')
def create_user():
    pass


@bp.get('/<int:user_id>')
def get_exact_user(user_id: int):
    pass


@bp.put('/<int:photo_id>')
def change_user_photo(photo_id: int):
    pass


@bp.delete('/<int:photo_id>')
def delete_user_photo(photo_id: int):
    pass
