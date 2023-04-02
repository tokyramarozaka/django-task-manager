from django.shortcuts import render

# Create your views here.

# TASKS
def get_all_tasks(request):
    return render(request, 'tasks.html', {})

def get_task_by_id(request, id):
    return render(request, 'single_task.html', {})

def get_tasks_by_category(request, id):
    return render(request, 'tasks.html', {})

def post_task(request):
    return render(request, 'tasks.html', {})

# CATEGORY
def get_all_categories(request):
    return render(request, 'categories.html', {})

def get_category_by_id(request, id):
    return render(request, 'single_category.html', {})

def post_category(request):
    return render(request, 'categories.html', {})