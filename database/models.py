import datetime

from main import db
from werkzeug.security import generate_password_hash, check_password_hash


# Таблица пользователя
class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String, nullable=False)
    first_name = db.Column(db.String, nullable=False)
    last_name = db.Column(db.String, nullable=True)
    email = db.Column(db.String, nullable=False)
    phone_number = db.Column(db.String, nullable=False, unique=True)
    about = db.Column(db.String, nullable=True)

    def register_user(self, username: str, first_name: str, last_name: str, email: str, phone_number: str, about: str):
        new_user = User(username=username, first_name=first_name, last_name=last_name, email=email,
                        phone_number=phone_number, about=about)

        db.session.add(new_user)
        db.session.commit()

    # Изменить имя
    def change_username(self, user_id: int, new_username: str):
        user = User.query.get_or_404(user_id)

        # Меняем имя
        if user.username == new_username:
            return 'Новое имя должно отличаться от старого'

        user.username = new_username

        db.session.commit()

    # Изменить номер телефона
    def change_phone_number(self, user_id: int, new_phone_number: str):
        user = User.query.get_or_404(user_id)

        if user.phone_number == new_phone_number:
            return 'Новый номер не должно совподать со старым'

        user.phone_number = new_phone_number

        db.session.commit()

    # Изменить email
    def change_email(self, user_id: int, new_email: str):
        user = User.query.get_or_404(user_id)

        if user.email == new_email:
            return 'Новый email не должно совподать со старым'

        user.email = new_email

        db.session.commit()

    # Изметь про себя
    def change_about(self, user_id: int, new_about: str):
        user = User.query.get_or_404(user_id)

        if user.about == new_about:
            return 'Новый текст не должно совподать со старым'

        user.about = new_about

        db.session.commit()


# Таблица постов
class Post(db.Model):
    __tablename__ = 'posts'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    header = db.Column(db.String, nullable=False)
    main_text = db.Column(db.String, nullable=False)
    publish_date = db.Column(db.DateTime)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    post_likes = db.Column(db.Integer, default=0)

    user = db.relationship('User')

    # Добавление поста
    def create_post(self, header: str, main_text: str, publish_date, user_id: int):
        new_post = Post(header=header, main_text=main_text, publish_date=publish_date, user_id=user_id)

        db.session.add(new_post)
        db.session.commit()

    # Изменить заголовок
    def change_header(self, post_id: int, new_header: str):
        current_post = Post.query.get_or_404(post_id)
        if current_post.header == new_header:
            return 'Новый заголовок не должен совподать со старым'

        current_post.header = new_header

        db.session.commit()

    # Изменить описание
    def change_main_text(self, post_id: int, new_main_text: str):
        current_post = Post.query.get_or_404(post_id)
        if current_post.main_text == new_main_text:
            return 'В новом тесксте нет никаких изменений'

        current_post.main_text = new_main_text

        db.session.commit()

    # Счетчик лайков для постов
    def likes_detect(self, post_id: int):
        current_post = Post.query.get_or_404(post_id)
        current_post.post_likes += 1
        db.session.commit()

    # Удалить пост
    def delete_post(self, post_id: int):
        current_post = Post.query.get_or_404(post_id)
        db.session.delete(current_post)
        db.session.commit()


# Таблица фото
class PhotoPost(db.Model):
    __tablename__ = 'photos_for_post'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    post_id = db.Column(db.Integer, db.ForeignKey('posts.id', ondelete='SET NULL'))
    photo_path = db.Column(db.String, nullable=False)

    post = db.relationship('Post')


class Comment(db.Model):
    __tablename__ = 'comments'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    text = db.Column(db.String, nullable=False)
    likes = db.Column(db.Integer, nullable=True, default=0)
    publish_date = db.Column(db.DateTime)
    post_id = db.Column(db.Integer, db.ForeignKey('posts.id', ondelete='SET NULL'))

    # Добавить комментарии
    def add_comment(self, text: str, post_id: int, publish_date):
        new_comment = Comment(text=text, post_id=post_id, publish_date=publish_date)

        db.session.add(new_comment)
        db.session.commit()

    # Изметь текс комментарии
    def change_text(self, comment_id: int, new_text: str):
        current_comment = Comment.query.get_or_404(comment_id)

        if current_comment.text == new_text:
            return 'Новый текст не должен совпадать со старым'

        current_comment.text = new_text

        db.session.commit()

    # Удалить коммент
    def delete_comment(self, comment_id: int):
        current_comment = Comment.query.get_or_404(comment_id)
        db.session.delete(current_comment)
        db.session.commit()

    # Счетчик лайков
    def likes_detect(self, comment_id: int):
        current_comment = Comment.query.get_or_404(comment_id)
        current_comment.likes += 1
        db.session.commit()


# Таблица хэштегов
class Hashtag(db.Model):
    __tablename__ = 'hashtags'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    hash_name = db.Column(db.String, nullable=False, unique=True)
    post_id = db.Column(db.Integer, db.ForeignKey('posts.id', ondelete='SET NULL'))

    post = db.relationship('Post')

    # Добавление хэштега
    def add_hashtag(self, hash_name: str, post_id: int):
        new_hashtag = Hashtag(hash_name=hash_name, post_id=post_id)

        db.session.add(new_hashtag)
        db.session.commit()


# Таблица паролей
class Password(db.Model):
    __tablename__ = 'passwords'
    password = db.Column(db.String, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id', ondelete='SET NULL'), primary_key=True)

    user = db.relationship('User')

    # Генерация пароля
    def set_password(self, password: str):
        self.password = generate_password_hash(password)

    # Проверка пароля
    def check_password(self, password: str):
        return check_password_hash(self.password, password)

    # Изменение пароля
    def change_password(self, user_id: int, new_password: str):
        user = Password.query.get_or_404(user_id)

        if user.password == new_password:
            return 'Старый пароль не должен совпадать с новым'

        user.password = new_password

        db.session.commit()
