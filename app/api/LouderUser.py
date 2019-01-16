from app import lm

from app.models.UsuarioObjeto import usuario


@lm.user_loader
def load_user(id):
    return usuario.query.filter_by(id=usuario.id).first()
