from django.http import HttpResponse
from django.template import Template, Context

import datetime

def saludo(request):
    return HttpResponse('Hola mundo Django')

def segunda_vista(request):
    return HttpResponse('<br><br>Ya Entendimos esto, es muy simple :)')

def diaDeHoy(request):
    dia = datetime.datetime.now()
    display_dia = f'Hoy es dia <br> {dia}'
    return HttpResponse(display_dia)

def mi_nombre_es(self, nombre):
    
    display_name = f'Mi nombre es: {nombre.capitalize()}'
    return HttpResponse(display_name)

def testing_template1(self):
    name = 'Valentino'
    surname = 'Paterno'
    
    dict = {'nombre': name, 'apellido': surname, 'date': datetime.datetime.now()} 
    template1_html = open('mysite/templates/template1.html')
    
    template = Template(template1_html.read())
    template1_html.close()

    context = Context(dict)
    document = template.render(context)
    return HttpResponse(document)


