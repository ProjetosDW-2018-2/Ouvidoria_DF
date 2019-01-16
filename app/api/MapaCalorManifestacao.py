import pymysql
from flask import render_template
from app import app
from app.controllers.ControleMPS import gerarMapadeCalor, gerarMapadePonto


@app.route('/mapa_calor_manifestacao')
def mapa_manifestacao():
    # se conecta com a base do DW
    conexao = pymysql.connect(host='www.db4free.net', user='alunoufrpe2', password='ufrpedwbi', db='ouvidoria_df', charset='utf8mb4')
    c = conexao.cursor()
    consuta = '''select latitude, longitude, descricao from dim_localizacao where Chave_Dimensao_Localizacao < 1000;'''
    c.execute(consuta)
    resporta = c.fetchall()
    gerarMapadeCalor(resporta, 'mapa_calor_manifestacao')
    gerarMapadePonto(resporta, 'mapa_calor_manifestacao_pontos')
    return render_template('mapa_calor_manifestacao.html')
