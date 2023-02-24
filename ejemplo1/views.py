from django.http import HttpResponse
import datetime
#request: para realizar peticiones 
#HttpResponse: Para ebviar la respuesta usando el protocolo HTTP.

def bienvenida(request):
    return HttpResponse("Bien venido a mi canal-222")

def bienvenidaRojo(request):
    return HttpResponse("<p style='color:red;'>Bien venido a mi canal-222</p>")

def categoriaEdad(request,edad):
    if edad>=18:
        if edad >=60:
            categoria="Tercera edad"
        else:
            categoria="Adultez"
    else:
        if edad<10:
            categoria="Infancia"
        else:
            categoria='Adolescencia'
    
    resultado='<h1>Categoria de la edad: %s</h>'%categoria
    return HttpResponse(resultado)

def obtenerMomentoActual(request):
    #respuesta="<h1>Momento actual: {0}</h1>".format(datetime.datetime.now())
    respuesta="<h1>Momento actual: {0}</h1>".format(datetime.datetime.now().strftime("%A %d/%m/%Y %H:%M:%S"))
    return HttpResponse(respuesta)