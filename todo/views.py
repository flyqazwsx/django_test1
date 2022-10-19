from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404

from todo.forms import TodoForm
from .models import Todo

# Create your views here.


def create_todo(request):

    form = TodoForm()
    if request.method == 'POST':
        print(request.POST)
        if request.user.is_authenticated:
            form = TodoForm(request.POST)
            todo = form.save(commit=False)
            todo.user = request.user
            todo.save()

            return redirect('todo')
    return render(request, './todo/createtodo.html', {'form': form})


def todo(request):
    todos = None
    # 確定有使用者登入
    if request.user.is_authenticated:
        todos = Todo.objects.filter(user=request.user)

    return render(request, './todo/todo.html', {'todos': todos})


def viewtodo(request, id):
    try:
        todo = get_object_or_404(Todo, id=id)
        return render(request, './todo/viewtodo.html', {'todo': todo})
    except Exception as e:
        print(e)
    return render(request, './todo/404.html')
