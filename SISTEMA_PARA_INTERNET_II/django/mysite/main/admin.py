from django.contrib import admin

# Register your models here.
from main.models import Item, ToDoList

admin.site.register(Item)
admin.site.register(ToDoList)