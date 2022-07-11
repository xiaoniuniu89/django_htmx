from django.db import models
from django.contrib.auth.models import User
from django.db.models.functions import Lower
# Create your models here.


class Todo(models.Model):
    todo_body = models.CharField(max_length=128)
    users = models.ManyToManyField(User, related_name='todos', through='UserTodos')
    
    class Meta:
        ordering = [Lower("todo_body")]

class UserTodos(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    todo = models.ForeignKey(Todo, on_delete=models.CASCADE)
    order = models.PositiveSmallIntegerField()
    
    class Meta:
        ordering = ['order']
    