from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Подключение базы данных
db = SQLAlchemy()
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///media.db'
<<<<<<< HEAD
app.config['UPLOAD_FOLDER'] = 'media'  #Указать путь для медиа
=======
app.config['UPLOAD_FOLDER'] = 'media'  # Указать путь для медиа компонента


db.init_app(app)

from comment import bp as comment_bp
from hashtag import bp as hashtag_bp
from posts import bp as posts_bp
from photo import bp as photo_bp
from user import bp as user_bp

from authentication import bp as auth

from authentication import bp as auth_bp


# Регистрация компонента
app.register_blueprint(comment_bp)
app.register_blueprint(hashtag_bp)
app.register_blueprint(posts_bp)
app.register_blueprint(photo_bp)
app.register_blueprint(user_bp)
<<<<<<< HEAD
app.register_blueprint(auth)
=======
app.register_blueprint(auth_bp)

>>>>>>> origin/main

@app.route('/hello')
def index():
    return 'Hello world'


app.run()
