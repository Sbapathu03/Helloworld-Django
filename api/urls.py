from django.urls import path
from .views import hello_world_json, hello_world_html

urlpatterns = [
    path('json/', hello_world_json, name='hello_world_json'),
    path('html/', hello_world_html, name='hello_world_html'),
]
