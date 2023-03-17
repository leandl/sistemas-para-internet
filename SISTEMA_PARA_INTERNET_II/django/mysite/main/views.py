from django.http import HttpResponseRedirect
from django.shortcuts import render

from .models import ToDoList
from .forms import CreateNewList
        

def get_todo_list(request, id):
    todo = ToDoList.objects.get(id=id)
    return render(request, 'main/list.html', { "todo": todo })

def home(request):
    return render(request, 'main/home.html', {})


def create(request):
    if request.method == "POST":
        form = CreateNewList(request.POST)
        
        if form.is_valid():
            name = form.cleaned_data["name"]
            todo = ToDoList(name=name)
            todo.save()
            
        return HttpResponseRedirect("/%i" % todo.id)
            
    
    form = CreateNewList()
    return render(request, 'main/create.html', { "form": form })