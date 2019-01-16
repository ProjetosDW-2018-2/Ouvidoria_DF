from app import db
from app.models.AcidenteObjeto import acidente
from app.models.EnderecoObjeto import endereco
from app.models.SemaforoObjeto import semaforo
from app.persistence.EnderecoDao import getEnderecoDao

def postAcidente(objAcidente):
    db.session.add(objAcidente)
    if db.session.commit() == None:
        return True  # objAcidente foi inserido no banco
    return False
def  getAcidentes():
    objAcidente = acidente.query.filter_by().all()
    if objAcidente == None:
        return None
    return objAcidente

def getAcidentesFiltro(stringData='', tipoDeDado=''):

    if stringData != '' and tipoDeDado !='':

        if tipoDeDado =='buscaData':
            objAcidente = acidente.query.filter((acidente.data_abertura.like('%'+stringData+'%')))
            if objAcidente == None:
                return None
            return objAcidente

        elif tipoDeDado =='buscaHora':
            objAcidente = acidente.query.filter((acidente.hora_abertura.like('%'+stringData+'%')))
            return objAcidente
            if objAcidente == None:
                return None

        elif tipoDeDado =='buscaTipoDeOcorrencia':
            objAcidente = acidente.query.filter((acidente.tipo_ocorrencia.like('%'+stringData+'%')))
            if objAcidente == None:
                return None
            return objAcidente

        elif tipoDeDado =='buscaTipo':
            objAcidente = acidente.query.filter((acidente.tipo.like('%'+stringData+'%')))
            if objAcidente == None:
                return None
            return objAcidente

        elif tipoDeDado == 'buscaQtd':
            objAcidente = acidente.query.filter((acidente.quantidade_vitimas.like('%' + stringData + '%')))
            if objAcidente == None:
                return None
            return objAcidente

        elif tipoDeDado == 'buscaLocal':
            objAcidente = acidente.query.join((endereco, acidente.endereco_codlocal == endereco.codlocal)).filter(
                endereco.local1.like('%' + stringData + '%'))
            if objAcidente == None:
                return None
            return objAcidente

        elif tipoDeDado == 'buscaLocalAcidenteSemaforo':
            objAcidente = endereco.query.outerjoin(acidente, semaforo).filter(endereco.local1.like('%' + stringData + '%'))
            if objAcidente == None:
                return None
            return objAcidente
    return None

def getAcidentesFiltro2(comp_select_ano, comp_select_mes, comp_select_bairro, comp_select_qtd_vitimas):
    objAcidente = acidente.query.join((endereco, acidente.endereco_codlocal == endereco.codlocal)).filter(
        endereco.local1.like('%' + comp_select_bairro + '%'),
        acidente.data_abertura.like('%' + comp_select_ano + '%'),
        acidente.data_abertura.like('%' + comp_select_mes + '%'),
        acidente.quantidade_vitimas.like('%' + comp_select_qtd_vitimas + '%'))

    if objAcidente == None:
        return None
    return objAcidente

def getAcidentesMes(ano=''):
    if ano != '':
        objAcidente = acidente.query.filter((acidente.data_abertura.like('%' + ano + '%')))
        if objAcidente == None:
            return None
        return objAcidente
    return None
