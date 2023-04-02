from django.shortcuts import render

from task.forms.task_form import TaskForm
from .models import Category, Task
from django.db.models import Q

# Create your views here.

# TASKS
def get_all_tasks(request):
    """ Retrieves all tasks in the database """
    tasks = Task.objects.all().order_by('deadline')
    return render(request, 'tasks.html', {
        'tasks' : tasks
    })

def get_task_by_id(request, id_task):
    """ Retrieves a single task by using its id """
    task = Task.objects.get(id=id_task)
    return render(request, 'single_task.html', {
        'task' : task,
    })

def get_tasks_by_category(request, id_category):
    """ Retrives all tasks corresponding to the given category id"""
    tasks = Task.objects.filter(category=id_category)
    return render(request, 'tasks.html', {
        'tasks' : tasks,
    })

def post_task(request):
    """ Creates and saves a new task into the database """
    if(request.method == 'POST'):
        form = TaskForm(request.POST)

        if form.is_valid() : 
            form.save()
        else : 
            form.errors.as_data()
        return render(request, 'create_task.html', {
            'message': 'Task added successfully'
        })
    else :
        raise (request, 'tasks.html', {})


# CATEGORY
def get_all_categories(request):
    categories = Category.objects.all().order_by('-category_priority')
    return render(request, 'categories.html', {
        'categories' : categories,
    })

def get_category_by_id(request, id_category):
    category = Category.objects.get(id=id_category)
    return render(request, 'single_category.html', {
        'category' : category,
    })

def post_category(request):
    return render(request, 'categories.html', {})