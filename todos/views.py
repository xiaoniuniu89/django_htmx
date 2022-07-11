from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods
from .models import Todo, UserTodos
from .utils import get_max_order, reorder

# Create your views here.
@login_required
def todos(request):
    user = request.user
    todos = UserTodos.objects.prefetch_related('todo').filter(user=user)
    return render(request, 'todos/todos.html', {'todos': todos})


# htmx views 

@login_required
def add_todo(request):
    todo_body = request.POST.get('todo')
    todo = Todo.objects.get_or_create(todo_body=todo_body)[0]

    if not UserTodos.objects.filter(todo=todo, user=request.user).exists():
        UserTodos.objects.create(todo=todo, user=request.user, order=get_max_order(request.user))
        
    todos = UserTodos.objects.filter(user=request.user)
    
    return render(request, 'todos/partials/todolist.html', {'todos': todos})


@login_required
@require_http_methods(['DELETE'])
def delete_todo(request, pk):
    UserTodos.objects.get(pk=pk).delete()
    request.user.todos.remove(pk)
    reorder(request.user)
    todos = UserTodos.objects.filter(user=request.user)
    return render(request, 'todos/partials/todolist.html', {'todos': todos})
        
@login_required    
def search_todos(request):
    search_text = request.POST.get('search')
    user_todos = UserTodos.objects.filter(user=request.user)
    results = Todo.objects.filter(todo_body__icontains=search_text).exclude(
        todo_body__in=user_todos.values_list('todo__todo_body', flat=True)
    )
    return render(request, 'todos/partials/search-results.html', {'results': results})

@login_required
def sort_todos(request):
    todo_pks_order = request.POST.getlist('todos-order')
    print(todo_pks_order)
    todos = []
    updated_todos = []
    
    user_todos = UserTodos.objects.prefetch_related('todo').filter(user=request.user)
    
    for index, todo_pk in enumerate(todo_pks_order, start=1):
        user_todo = next(u for u in user_todos if u.pk == int(todo_pk))
        
        if user_todo.order != index:
            user_todo.order = index
            updated_todos.append(user_todo)
        
        
        todos.append(user_todo)
        
    UserTodos.objects.bulk_update(updated_todos, ['order'])
    return render(request, 'todos/partials/todolist.html', {'todos': todos})
