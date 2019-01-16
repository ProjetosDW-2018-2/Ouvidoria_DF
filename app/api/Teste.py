from app import app
import csv,codecs
import pymysql
from  flask import render_template, request
from  datetime import  datetime
from pymysql import cursors

@app.route("/teste")
def teste():
    conexao = pymysql.connect(host='www.db4free.net', user='alunoufrpe2', password='ufrpedwbi', db='ouvidoria_df')
    c = conexao.cursor()
    consuta = '''select * from usuario;'''
    c.execute(consuta)
    resporta = c.fetchall()
    #consulta = '' #''''insert into rpa (id_rpa,nome) values (111,minhaJeba)'''
    #c.execute(consulta)
    return (str(resporta))

