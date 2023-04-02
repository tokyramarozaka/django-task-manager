from django.shortcuts import render
from django.db.models import Q
from task.forms.task_form import TaskForm
from .models import Category, Task

# Create your views here.

# TASKS
def get_all_tasks(request):
    """ Retrieves all tasks in the database """
    tasks = Task.objects.all().order_by('deadline')
    return render(request, 'tasks.html', {
        'tasks' : tasks,
        'label' : 'All Tasks'
    })

def get_task_by_id(request, id_task):
    """ Retrieves a single task by using its id """
    task = Task.objects.get(id=id_task)
    return render(request, 'tasks_single.html', {
        'task' : task,
    })

def get_tasks_by_category(request, id_category):
    """ Retrives all tasks corresponding to the given category id"""
    tasks = Task.objects.filter(category=id_category)
    category = Category.objects.get(id=id_category)

    return render(request, 'tasks.html', {
        'tasks' : tasks,
        'label' : 'All '+ category.category_name +' tasks'
    })

def post_task(request):
    """ Creates and saves a new task into the database """
    if(request.method == 'POST'):
        form = TaskForm(request.POST)

        if form.is_valid() : 
            form.save()
        else : 
            form.errors.as_data()
        return render(request, 'tasks_create.html', {
            'message': 'Task added successfully',
            'form': form
        })
    else :
        form = TaskForm()
        return render(request, 'tasks_create.html', {
            'form': form,
        })

def get_task_by_title_or_description(request):
    """ Searches all tasks whose title or description contains the given keyword """
    keyword = request.GET.get("q")
    results = Task.objects.filter(
        Q(task_title__icontains=keyword) | Q(task_description__icontains=keyword)
    )

    # Ternary operator is so weird ... I know.
    label = 'All tasks' if keyword.strip()=='' else 'Search results for '+keyword

    return render(request, 'tasks.html', {
        'label' : label, 
        'tasks': results,
    })


# CATEGORY
def get_all_categories(request):
    categories = Category.objects.all().order_by('-category_priority')
    return render(request, 'categories.html', {
        'categories' : categories,
    })

def get_category_by_id(request, id_category):
    category = Category.objects.get(id=id_category)
    return render(request, 'categories_single.html', {
        'category' : category,
    })

# Todo : make posting new categories possible and build its form
def post_category(request):
    return render(request, 'categories_create.html', {})