import pymysql
from flask import render_template, url_for, flash, request
from werkzeug.utils import redirect
from app.controllers.ControleMPS import gerarMapadeCalor
from app.controllers.PesquisaForms import pesquisaForm
from app import app

@app.route('/filtro', methods=["GET",'POST'])
def filtro():
    conexao = pymysql.connect(host='www.db4free.net', user='alunoufrpe2', password='ufrpedwbi', db='ouvidoria_df', charset='utf8mb4')
    c = conexao.cursor()
    form = pesquisaForm()
    comp_select_ano = request.form.get('comp_select_ano')
    comp_select_tema = request.form.get('comp_select_tema')
    comp_select_sexo = request.form.get('comp_select_sexo')
    comp_select_tipo_resposta = request.form.get('comp_select_tipo_resposta')
    comp_select_situacao_manifestacao = request.form.get('comp_select_situacao_manifestacao')
    lista = [comp_select_ano, comp_select_tema, comp_select_sexo, comp_select_tipo_resposta, comp_select_situacao_manifestacao]
    cont = 0
    for i in lista:
        if i != None and i != "":
            cont += 1
    if cont > 4:
        consulta = "select coordenada_X, coordenada_Y, descricaoLocalizacao as Endereco, idTemaNoAssunto,idtema, descricao as DescricaoTema," \
                   +" DescricaoTipoSituacao from (select l.coordenada_X, l.coordenada_Y,l.descricao as descricaoLocalizacao, a.tema_idtema as idTemaNoAssunto," \
                   +" sm.descricao as DescricaoTipoSituacao from manifestacao as man" \
                   +" inner join localizacao as l " \
                   +" on l.idlocalizacao = man.localizacao_idlocalizacao" \
                   +" inner join resposta r on man.idmanifestacao = r.manifestacao_idmanifestacao"\
                   +" inner join sexo as s " \
                   +" on s.idsexo = man.sexo_idsexo" \
                   +" inner join assunto as a " \
                   +" on a.idassunto = man.assunto_idassunto" \
                   +" inner join situacao_manifestacao  sm " \
                   +" on sm.idsituacao_manifestacao = man.situacao_manifestacao_idsituacao_manifestacao"\
                   +" where man.anoAbertura =" + comp_select_ano + " and man.sexo_idsexo =" + comp_select_sexo \
                   +" and sm.idsituacao_manifestacao ="+ comp_select_situacao_manifestacao \
                   +" and r.tipoResposta = '" + comp_select_tipo_resposta + "') as Resultado " \
                   +" inner join tema as t " \
                   +" on t.idtema = Resultado.idTemaNoAssunto " \
                   +" where  idTemaNoAssunto = "+ comp_select_tema +";"
        c.execute(consulta)
        resposta = c.fetchall()
        if resposta!= None:
            gerarMapadeCalor(resposta, 'mapa_manifestacao_filtro')
            return redirect(url_for('mapa_manifestacao_filtro'))
        flash('Filtro incorreto.', 'erro')
        return render_template('filtro.html', form=form)
    return render_template('filtro.html', form=form)
