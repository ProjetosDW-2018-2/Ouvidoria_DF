from flask import render_template, redirect, url_for, flash
from app import app
from app.controllers.ContatoForms import ContatoForm
from flask_mail import Message, Mail

mail = Mail(app)
app.config["MAIL_SERVER"] = "smtp.gmail.com"
app.config["MAIL_PORT"] = 465
app.config["MAIL_USE_SSL"] = True
app.config["MAIL_USERNAME"] = 'projetoanalise2018.1@gmail.com'
app.config["MAIL_PASSWORD"] = 'analise2018'
app.config["MAIL_USE_TLS"] = False

mail.init_app(app)

if __name__ == '__main__':
   app.run(debug = True)

@app.route('/contato', methods=["GET", "POST"])
def contato():
    form = ContatoForm()
    if form.validate_on_submit():
        sender1 = str(form.email.data)
        msg = Message(str(form.nome.data), sender=sender1, recipients=['projetoanalise2018.1@gmail.com'])
        msg.body = """ De: %s\n\n Entidade do tipo: %s\n\n E-mail: %s\n\n Mensagem: %s\n\n
        """ % (str(form.nome.data), str(form.entidade.data), str(form.email.data), str(form.mensagem.data))
        mail.send(msg)
        flash ("Mensagem enviada com sucesso!")
        return redirect(url_for('index'))
    else:
        return render_template('contato.html', form=form)
