from django.http import HttpResponse
from django.template import Template,Context
import os
import datetime

def index(request):
    
    #parametros de usuario 
    Nombre = "saul burciaga hernandez"
    NumeroControl = "17030078"
    Semestre = 7
    FechaIngreso = datetime.datetime.now()

    #parametros de contrato
    NumeroContrato = 1
    Pago = 500
    FechaPago= datetime.datetime.now()


    #parametro de peliculas 
    NombrePelicula = "insurgente"
    Duracion = "1 hora con 10 minutos"
    FechaSalida = "08/02/1998"

    #parametro de anime
    NombreAnime = "Dora La Exploradora aun que no sea anime ay se va xd"
    CapitulosAnime = 12
    TemporadaAnime = 1
    FechaAnime = datetime.datetime.now()

    #abrir archivos remderizar y conllevar contexto
    archivo_html = open(os.path.dirname(os.path.realpath(__file__))+"/html/index.html","r")
    plt=Template(archivo_html.read())
    archivo_html.close()
    ctx_index=Context({
        "Nombre":Nombre,"NumeroControl":NumeroControl,"Semestre":Semestre,"FechaIngreso":FechaIngreso,
        "NumeroContrato":NumeroContrato, "Pago":Pago,"FechaPago":FechaPago,
        "NombrePelicula":NombrePelicula, "Duracion":Duracion,"FechaSalida":FechaSalida,
        "NombreAnime":NombreAnime,"CapitulosAnime":CapitulosAnime,"TemporadaAnime":TemporadaAnime,"FechaAnime":FechaAnime
    
    })
    index_html = plt.render(ctx_index)
    
    return HttpResponse(index_html)