from django.shortcuts import render
from django_user_agents.utils import get_user_agent

# Create your views here.

def home (request):
    user_agent = get_user_agent(request)
    if user_agent.is_mobile:
        file = "Hola eres un telefono móvil"
    elif user_agent.is_pc:
        file = "Hola eres un pc"
    elif user_agent.is_tablet:
        file = "Hola eres una tablet"

    return render(request, 'core/home.html', {"data" : file})
