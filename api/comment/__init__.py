from flask import Blueprint


bp = Blueprint('comments', __name__, url_prefix='comment')


@bp.get('/<int:post_id>')
def get_comment_by_post_id(post_id: int):
    pass


@bp.post('/<int:post_id>')
def create_comment_to_post_by_post_id(post_id: int):
    pass


@bp.put('/<int:post_id>')
def change_comment_to_post_by_post_id(post_id: int):
    pass


@bp.delete('/<int:post>')
def delete_comment_from_post_by_post_id(post_id: int):
    pass
