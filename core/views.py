from django.shortcuts import render
from django_user_agents.utils import get_user_agent
from django.http import FileResponse
from django.http import HttpResponse
import os

# Create your views here.
path = os.path.realpath('C:/Users/Usuario/Desktop/file.png')

def home (request):
    
    user_agent = get_user_agent(request)
    if user_agent.is_mobile:
        message = "Descarga la app desde tu teléfono móvil"

    else:
        message = "Genera código QR para descargar la app"
        
    return render(request, 'core/home.html', {"data" : message})

def download (path):
    file = open(path,"rb")
    response = FileResponse(file) 
    response["Content-disposition"] = "attachment; filename={}".format(os.path.basename(path))
    return response