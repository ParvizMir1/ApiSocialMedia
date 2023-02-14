from flask import Blueprint
from flask_restx import Resource, Api
from database.models import PhotoPost
from werkzeug.datastructures import FileStorage
import os
from werkzeug.utils import secure_filename

bp = Blueprint('photo', __name__, url_prefix='/photos')
api = Api(bp)

photo_model = api.parser()
photo_model.add_argument('new_photo', type=FileStorage, location='files')

@api.route('/photo')  # get/post
class GetAllPhotos(Resource):
    def get(self):
        photo = PhotoPost.query.all()
        result = [{i.post_id: i.photo_path} for i in photo]
        return {'status': 1, 'result': result}


@api.route('/<int:photo_id>')  # put/delete
class ChangeOrDeletePhoto(Resource):
    def get(self, photo_id: int):
        current_photo = PhotoPost.query.get_or_404(photo_id)
        if current_photo:
            return {'status': 1,
                    'photo': {'post_id': current_photo.id,
                              'photo_location': current_photo.photo_path}}

        return {'status': 0, 'message': 'Нет такой фотографии'}

    def put(self, photo_id: int):
        args = photo_model.parse_args()
        new_photo = args.get('new_photo')

        new_photo.save(os.path.join('media/', secure_filename(new_photo.filename)))
        PhotoPost().change_post_image(photo_id, new_photo.filename)

        return {'status': 1, 'message': 'Фото успешно измененно'}


    def delete(self, photo_id: int):
        PhotoPost().delete_post_image(photo_id)

        return {'status': 1, 'message': 'Фото успешно удалено'}
