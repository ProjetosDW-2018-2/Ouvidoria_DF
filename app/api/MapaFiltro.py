from flask import render_template
from app import app

@app.route('/mapa_manifestacao_filtro')
def mapa_manifestacao_filtro():
    return render_template('mapa_manifestacao_filtro.html')
