import folium
from folium import plugins
from folium.plugins import MarkerCluster
from folium.plugins import Draw

import shutil
import os

def moverArquivo(nomeDoArquivo, diretorio='app/tempalates'):
    if shutil.move(nomeDoArquivo + '.html', diretorio):
        print("Arquivo  MOVIDO da pasta controllers para template")
        return True
    return False

def deletarAquivo(nomeDoArquivo,  diretorio='app/tempalates'):
    dir = os.listdir(diretorio)
    for file in dir:
        if file == nomeDoArquivo + '.html':
            os.remove(file)
            print("Arquivo deletado com sucesso.")
            return True
    return False

def gerarMapadePonto(listaDeCoordenadas, nomeDoMapa):

    mapa = folium.Map(location=[-15.78018, -47.929215],zoom_start=13)
    marker_cluster = MarkerCluster().add_to(mapa)
    draw = Draw()
    draw.add_to(mapa)
    x=[]
    y=[]
    z=[]
    for linha in listaDeCoordenadas:
        x.append(float(linha[0]))
        y.append(float(linha[1]))
        z.append(linha[2])

    listaLatitudesLongitudes1 =[x, y, z]
    if listaLatitudesLongitudes1 != None:
        for la,lo, rua in zip(listaLatitudesLongitudes1[0], listaLatitudesLongitudes1[1], listaLatitudesLongitudes1[2]):
            folium.Marker(location=[la, lo], popup=rua, icon=folium.Icon(color='red')) .add_to(marker_cluster)
    mapa.save('app/templates/' + nomeDoMapa + ".html")

def gerarMapadeCalor(listaDeCoordenadas, nomeDoMapa):
    x=[]
    y=[]
    for linha in listaDeCoordenadas:
        x.append(float(linha[0]))
        y.append(float(linha[1]))

    listaLatitudesLongitudes1 =[x, y]
    mapa_calor = folium.Map(location=[-15.78018, -47.929215], zoom_start=13)
    lCoordenadas =[]
    if listaLatitudesLongitudes1 != None:
        for la,lo in zip(listaLatitudesLongitudes1[0],listaLatitudesLongitudes1[1]):
            lCoordenadas.append([la,lo])

        mapa_calor.add_child(plugins.HeatMap(lCoordenadas))
        mapa_calor.save('app/templates/' + nomeDoMapa + ".html")