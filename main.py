from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Подключение базы данных
db = SQLAlchemy()
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///media.db'
db.init_app(app)

from comment import bp as comment_bp
from hashtag import bp as hashtag_bp
from posts import bp as posts_bp
from photo import bp as photo_bp
from user import bp as user_bp

# Регистрация компонента
app.register_blueprint(comment_bp)
app.register_blueprint(hashtag_bp)
app.register_blueprint(posts_bp)
app.register_blueprint(photo_bp)
app.register_blueprint(user_bp)


@app.route('/hello')
def index():
    return 'Hello world'


app.run()
