from flask import render_template, redirect, url_for, flash
from app import app
from app.models.UsuarioObjeto import usuario
from app.controllers.CadastroForms import CadastroForm
from app.controllers.UserControllers import valida_user, inserirUser, getIdMax


@app.route('/cadastro', methods=["GET", "POST"])
def cadastro():
    form = CadastroForm()
    if form.validate_on_submit():
        objUser = usuario(form.mail.data, form.password.data)
        id_user_maximo = getIdMax() + 1
        objUser.setId(id_user_maximo)

        if valida_user(objUser) == False:
            inserirUser(objUser)
            print('Usuario cadastrado com sucesso!')
            return redirect(url_for('index'))
        print('Usuario não cadastrado!')
        flash('Usuario não cadastrado.', 'erro')
    return render_template('cadastro.html', form=form)

