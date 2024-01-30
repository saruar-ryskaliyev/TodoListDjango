from django.shortcuts import render, redirect
from .models import ToDo



def index(request):
    todo = ToDo.objects.all()

    if request.method == 'POST':
        new_todo = ToDo(title = request.POST['title'], description = request.POST['description'], deadline = request.POST['deadline'])
        new_todo.save()
        return redirect('/')

    return render(request, "index.html", {'todos': todo})


def delete(request, pk):
    todo = ToDo.objects.get(id = pk)
    todo.delete()
    return redirect('/')