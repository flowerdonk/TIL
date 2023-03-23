from django.shortcuts import render, redirect
from .forms import TodoForms
from .models import Todo
from django.contrib.auth.decorators import login_required

def index(request):
    form = TodoForms()
    todo_list = Todo.objects.all() # 모든 Todo 데이터 조회
    context = {
        'form' : form,   
        'todo_list' : todo_list,
    }
    return render(request, 'todos/index.html', context)

def create(request):
    if request.method == 'POST':
        form = TodoForms(request.POST)
        if form.is_valid(): # 유효성 검사 -> clean_field를 거친 cleaned_data(dict)가 나옴
            form.save()
        
        return redirect('todos:index')

@ login_required
def update(request, pk):
    todo = Todo.objects.get(pk=pk)
    if request.method == 'POST':
        form = TodoForms(request.POST, instance=todo)
        if form.is_valid():
            form.save()
            return redirect('todos:index')
    else:
        form = TodoForms(instance=todo)

    context = {
        'form' : form,
        'todo' : todo,
    }
    return render(request, 'todos/update.html', context)

def delete(request, pk):
    if request.method == 'POST':
        todo = Todo.objects.get(pk=pk)
        todo.delete()
    return redirect('todos:index')

def done(request, pk):
    # Auth가 있다면? 
    todo = Todo.objects.get(pk=pk)
    todo.isCompleted = True
    todo.save()

    return redirect('todos:index')

