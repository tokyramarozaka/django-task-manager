from django.contrib import admin
from task.models import Category, Task 

# Register your models here.
admin.site.register(Category)
admin.site.register(Task)