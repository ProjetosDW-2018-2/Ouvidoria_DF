from app import db
class usuario(db.Model):
    __tablename__ = "usuario"
    id = db.Column(db.Integer, primary_key=True, autoincrement=False)
    email = db.Column(db.String(40), unique=True)
    password = db.Column(db.String(16))

    def __init__(self, email, password):
        self.email = email
        self.password = password

    @property
    def is_authenticated(self):
        return True

    @property
    def is_active(self):
        return True

    @property
    def is_anonymous(self):
        return False

    def get_id(self):
        return str(self.id)

    def setId(self, id):
        self.id = id

