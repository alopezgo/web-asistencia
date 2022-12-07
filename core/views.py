from django.shortcuts import render
from django_user_agents.utils import get_user_agent
from django.http.response import HttpResponse, Http404
import os


# Django project base directory
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def home (request):
    user_agent = get_user_agent(request)
    if user_agent.is_pc:
        message = "Descarga la app desde tu teléfono móvil"
    else:
        message = "Genera código QR para descargar la app"  
    return render(request, 'core/home.html', {"data" : message})

def download_apk(request):
    file_name = 'app-debug.apk'
    full_path = BASE_DIR + '/core/files/apk/' + file_name
    if os.path.exists(full_path):
        with open(full_path, 'rb') as fh:
            response = HttpResponse(fh.read(), content_type="application/force_download")
            response['Content-Disposition'] = 'inline; filename=' + os.path.basename(full_path)
            return response
    raise Http404


