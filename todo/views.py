from email import message
from turtle import Turtle
from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from todo.forms import TodoForm
from .models import Todo
from datetime import datetime


@login_required
def completed_by_id(request, id):
    # 篩選已完成項目
    todo = Todo.objects.get(id=id)
    todo.completed = not todo.completed
    todo.date_completed = datetime.now() if todo.completed else None
    todo.save()

    return redirect('todo')


@login_required
def delete(request, id):
    todo = Todo.objects.get(id=id)
    todo.delete()
    return redirect('todo')


@login_required
def completed(request):
    todos = Todo.objects.filter(user=request.user, completed=True)
    return render(request, './todo/completed.html', {'todos': todos})


@login_required
def create_todo(request):
    message = ''
    form = TodoForm()
    try:
        if request.method == 'POST':
            print(request.POST)
            if request.user.is_authenticated:
                form = TodoForm(request.POST, request.FILES)
                todo = form.save(commit=False)
                todo.user = request.user
                todo.date_completed = datetime.now() if todo.completed else None
                todo.save()

                return redirect('todo')
    except Exception as e:
        print(e)
        message = '資料輸入錯誤，請重新輸入'
    return render(request, './todo/createtodo.html', {'form': form, 'message': message})


@login_required
def sorttodo(request):
    try:
        todos = Todo.objects.filter(user=request.user)
        # None
        sort = request.COOKIES.get('sort')
        print(sort)

        sort = '1' if not sort or sort == '0' else '0'

        if sort == '1':
            todos = todos.order_by('-created')

    except Exception as e:
        print(e)

    response = render(request, './todo/todo.html', {'todos': todos})
    response.set_cookie('sort', sort)

    return response


def todo(request):
    todos = None
    # 確定有使用者登入
    if request.user.is_authenticated:
        todos = Todo.objects.filter(user=request.user, completed=False)

    return render(request, './todo/todo.html', {'todos': todos})


@login_required
def viewtodo(request, id):
    try:
        todo = Todo.objects.get(id=id)
        if request.method == 'GET':
            form = TodoForm(instance=todo)

        elif request.method == 'POST':
            print(request.POST)
            # 更新
            if request.POST.get('update'):
                # 將POST回傳值填入todo,產生Form表單
                form = TodoForm(request.POST, request.FILES, instance=todo)
                if form.is_valid():
                    # 資料暫存
                    todo = form.save(commit=False)
                    # 更新完成日期
                    todo.date_completed = datetime.now() if todo.completed else None
                    # 更新資料
                    form.save()
            # 刪除之後馬上回首頁
            elif request.POST.get('delete'):
                todo.delete()
                return redirect('todo')

        return render(request, './todo/viewtodo.html', {'todo': todo, 'form': form})
    except Exception as e:
        print(e)

    return render(request, './todo/404.html')
