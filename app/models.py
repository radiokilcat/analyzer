from app import app, db, login
from werkzeug.security import generate_password_hash, check_password_hash

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    reset_password = db.Column(db.Boolean, default=False)

    def __repr__(self):
        return '<User {}>'.format(self.username)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    @staticmethod
    def create_default_user():
        if User.query.first() is None:
            user = User(username=app.config['DEFAULT_USER']['username'],
                        reset_password=True)
            user.set_password(app.config['DEFAULT_USER']['password'])
            db.session.add(user)
            db.session.commit()


@login.user_loader
def load_user(id):
    return User.query.get(int(id))

def init_db():
    db.create_all()
    User.create_default_user()
