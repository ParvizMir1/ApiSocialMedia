from flask import Blueprint

bp = Blueprint('posts', __name__, url_prefix='/post')


@bp.get('/')
def all_posts():
    pass


@bp.post('/')
def create_post():
    pass


@bp.get('/<int:post_id>')
def get_exact_post(post_id: int):
    pass


@bp.put('/<int:post_id>')
def change_post_by_id(post_id: int):
    pass


@bp.delete('/<int:post_id>')
def delete_post_by_id(post_id: int):
    pass
