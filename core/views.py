from django.shortcuts import render
from django_user_agents.utils import get_user_agent
from django.http import FileResponse
from django.http import HttpResponse, Http404
import os

# Create your views here.
path = os.path.realpath('C:/Users/Usuario/Desktop/file.png')

# def home (request):
    
#     user_agent = get_user_agent(request)
#     if user_agent.is_pc:
#         message = "Descarga la app desde tu teléfono móvil"

#     else:
#         message = "Genera código QR para descargar la app"
        
#     return render(request, 'core/home.html', {"data" : message})

def home (request):
    
    user_agent = get_user_agent(request)
    if user_agent.is_pc:
        message = "Descarga la app desde tu teléfono móvil"

    else:
        message = "Genera código QR para descargar la app"
        
    return render(request, 'core/home.html', {"data" : message})

# Django project base directory
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Download APK file

def download_apk(file_base_name):
    print('Download ' + file_base_name + '.apk...')
    # Full path of file
    file_path = BASE_DIR + '/core/files/apk/' + file_base_name + '.apk'
    if os.path.exists(file_path):
        with open(file_path, 'rb') as fh:
            response = HttpResponse(fh.read(), content_type="application/force_download")
            response['Content-Disposition'] = 'inline; filename=' + os.path.basename(file_path)
            return response
    # If file is not exists
    raise Http404('File not found')

# def download (path):
#     file = open(path,"rb")
#     response = FileResponse(file) 
#     response["Content-disposition"] = "attachment; filename={}".format(os.path.basename(path))
#     return response



