from django.conf import settings
from django.core.wsgi import get_wsgi_application
from django.urls import path
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.template import loader
from django.conf.urls.static import static
import os
import sys
import django

from application.services import TaskService

# Huvudklassen som hanterar Django-konfiguration och servern
class TaskDjango:
    def __init__(self, service: TaskService):
        # TaskService-instansen injiceras för att hantera affärslogiken
        self.service = service
        self._configure_django()
        self._setup_urls()

    def _configure_django(self):
        # Konfigurera Django-inställningar programmatiskt
        # Detta är särskilt användbart när Django körs som en del av en större applikation
        settings.configure(
            DEBUG=True,  # Aktiverar debug-läge för utveckling
            SECRET_KEY='your-secret-key',  # Används för säkerhetsfunktioner
            ROOT_URLCONF=__name__,  # Anger denna modul som rot-URL-konfiguration
            MIDDLEWARE=[
                # Lista över middleware-klasser som behandlar requests/responses
                'django.middleware.security.SecurityMiddleware',
                'django.contrib.sessions.middleware.SessionMiddleware',
                'django.middleware.common.CommonMiddleware',
                'django.middleware.csrf.CsrfViewMiddleware',
                'django.contrib.auth.middleware.AuthenticationMiddleware',
                'django.contrib.messages.middleware.MessageMiddleware',
                'django.middleware.clickjacking.XFrameOptionsMiddleware',
            ],
            INSTALLED_APPS=[
                # Django-apps som behövs för grundläggande funktionalitet
                'django.contrib.auth',
                'django.contrib.contenttypes',
                'django.contrib.sessions',
                'django.contrib.messages',
                'django.contrib.staticfiles',
            ],
            TEMPLATES=[
                {
                    # Konfiguration för template-systemet
                    'BACKEND': 'django.template.backends.django.DjangoTemplates',
                    'DIRS': [os.path.join(os.path.dirname(__file__), 'templates')],
                    'APP_DIRS': True,
                    'OPTIONS': {
                        'context_processors': [
                            'django.template.context_processors.debug',
                            'django.template.context_processors.request',
                            'django.contrib.auth.context_processors.auth',
                            'django.contrib.messages.context_processors.messages',
                        ],
                    },
                },
            ],
            STATIC_URL='/static/',  # URL-prefix för statiska filer
            STATICFILES_DIRS=[os.path.join(os.path.dirname(__file__), 'static')],  # Sökvägar till statiska filer
        )
        django.setup()  # Initialiserar Django

    def _setup_urls(self):
        # Gör service-instansen tillgänglig globalt för vyerna
        global task_service
        task_service = self.service

    def run(self, host='127.0.0.1', port=8000):
        # Startar utvecklingsservern
        from wsgiref.simple_server import make_server
        application = get_wsgi_application()
        httpd = make_server(host, port, application)
        print(f"Starting Django server at http://{host}:{port}/")
        httpd.serve_forever()


# Vy-funktioner som hanterar HTTP-requests
def task_list(request):
    # Hämtar alla uppgifter och renderar dem i template
    tasks = task_service.get_all_tasks()
    return render(request, 'tasks/list.html', {'tasks': tasks})

def add_task(request):
    # Hanterar både GET (visa formulär) och POST (skapa ny uppgift)
    if request.method == 'POST':
        title = request.POST.get('title', '').strip()
        priority = request.POST.get('priority', 'medium')
        if title:
            task_service.create_task(title=title, priority=priority)
        return HttpResponseRedirect('/')
    return render(request, 'tasks/add.html')

def mark_completed(request, task_id):
    # Markerar en uppgift som slutförd
    task_service.mark_complete(task_id)
    return HttpResponseRedirect('/')

    # Deletes Tasks.
def delete(request, task_id):
      task_service.delete_task(task_id)
      return HttpResponseRedirect('/')
  
def toggle_complete(request, task_id):
    task = task_service.get_task_by_id(task_id)
    if task:
        task.completed = not task.completed
        task_service.update_task(task)
        return HttpResponseRedirect('/')

        

# URL-mönster som mappar URL:er till vy-funktioner
urlpatterns = [
    path('', task_list, name='task_list'),  # Startsidan visar alla uppgifter
    path('add/', add_task, name='add_task'),  # Sida för att lägga till uppgifter
    path('mark_completed/<int:task_id>/', mark_completed, name='mark_completed'),  # URL för att markera uppgifter som klara
    path('delete/<int:task_id>/', delete, name='delete_task'),
    path('toggle_complete/<int:task_id>/', toggle_complete, name='toggle_complete'),
]