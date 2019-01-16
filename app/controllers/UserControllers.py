from flask_login import login_user

from app.persistence.UserDao import getUserDao, postUser, getIdMaxDao


def valida_user(objUser):
    if getUserDao(objUser) == False:
        return False  # login errado
    print(login_user(objUser))
    return True  # usuario já cadastrado


def inserirUser(objUser):
    if postUser(objUser):
        return True  # cadastro ok
    return False  # cadastro não ok


def getUser(objUser):
    user = getUserDao(objUser)
    if user == False:
        return False  # login errado
    return user  # usuario já cadastrado


def getIdMax():
    id = getIdMaxDao()
    if id == False:
        return 0  # login errado
    return id  # usuario já cadastrado
