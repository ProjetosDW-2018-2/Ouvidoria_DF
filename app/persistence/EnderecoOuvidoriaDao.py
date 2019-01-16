from app import db
from app.models.EnderecoOuvidoria import EnderecoOuvidoria


def getEnderecoDao(endereco, latitude, longitude, descricao):
    objEndereco = EnderecoOuvidoria.query.filter(EnderecoOuvidoria.id_endereco == endereco,
                                        EnderecoOuvidoria.latitude == latitude,
                                        EnderecoOuvidoria.longitude == longitude,
                                        EnderecoOuvidoria.des_endereco == descricao)
    if objEndereco == None:
        return False  # não tem esse endereco no banco
    return objEndereco

def postEndereco(objEndereco):
    db.session.add(objEndereco)
    if db.session.commit() == None:
        return True  # endereco foi inserido no banco
    return False
