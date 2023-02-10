from flask import Blueprint

from comment import bp as comment_bp
from hashtag import bp as hashtag_bp
from posts import bp as posts_bp
from photo import bp as photo_bp
from user import bp as user_bp

bp = Blueprint('api', __name__, url_prefix='/api')

bp.register_blueprint(comment_bp)
bp.register_blueprint(hashtag_bp)
bp.register_blueprint(posts_bp)
bp.register_blueprint(photo_bp)
bp.register_blueprint(user_bp)
