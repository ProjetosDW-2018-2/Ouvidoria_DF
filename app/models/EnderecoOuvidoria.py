from app import db

class EnderecoOuvidoria(db.Model):
    __tablename__ = "endereco"

    id_endereco = db.Column(db.Integer, primary_key=True, autoincrement=True)
    latitude = db.Column(db.String(30))
    longitude = db.Column(db.String(30))
    des_endereco = db.Column(db.String(100))

    def __init__(self, id_endereco, latitude, longitude, des_endereco):
        self.id_endereco = id_endereco
        self.latitude = latitude
        self.longitude = longitude
        self.des_endereco = des_endereco
