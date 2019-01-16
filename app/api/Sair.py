from flask import flash, redirect, url_for
from app import app
from flask_login import logout_user


@app.route('/sair')
def sair():
    logout_user()
    print('Saindo da aplicação.')
    return redirect(url_for('index'))
