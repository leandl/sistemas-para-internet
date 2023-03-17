from django.urls import path
from . import views

urlpatterns = [
    path('create', views.create, name="create"),
    path('<int:id>', views.get_todo_list, name="get_todo_list"),
    path('', views.home, name="home"),
]
