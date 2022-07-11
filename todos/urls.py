from django.urls import path
from .views import (
    todos,
    add_todo,
    delete_todo,
    search_todos,
    sort_todos
)


urlpatterns = [
    path('', todos, name='todos' ),
    
]

htmx_url_patterns = [
    path('add-todo/', add_todo, name='add-todo'),
    path('delete-todo/<int:pk>/', delete_todo, name='delete-todo'),
    path('search/', search_todos, name='search_todos'),
    path('sort/', sort_todos, name='sort_todos'),
]


urlpatterns += htmx_url_patterns