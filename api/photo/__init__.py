from flask import Blueprint


bp = Blueprint('photo', __name__, url_prefix='/photo')


@bp.get('/')
def get_photos():
    pass


@bp.post('/')
def create_photo():
    pass


@bp.get('/<int:photo_id>')
def get_photo_by_id(photo_id: int):
    pass


@bp.put('/<int:photo_id>')
def change_photo_by_id(photo_id: int):
    pass


@bp.delete('/<int:photo_id>')
def delete_photo_by_id(photo_id: int):
    pass
