from django.contrib import admin
from django.urls import path
from escola.views import aluno

urlpatterns = [
    path('admin/', admin.site.urls),
    path('aluno/', aluno),
]
