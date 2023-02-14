from flask import Blueprint


bp = Blueprint('hashtag', __name__, url_prefix='/hashtag')


@bp.post('/')
def create_hashtag():
    pass


@bp.get('/')
def get_some_hashtags(size: int = 20, page: int = 1):
    pass


@bp.get('/<string:hashtag_name>')
def get_hashtag_by_name(hashtag_name: str):
    pass
