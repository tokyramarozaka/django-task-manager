"""task_manager URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from task import views as task

urlpatterns = [
    path('admin/', admin.site.urls),


    # All tasks routes
    path('tasks/', task.get_all_tasks, name='all_tasks'),
    path('task/create', task.post_task, name='create_task'),
    path('task/<int:id_task>/', task.get_task_by_id, name='single_task'),
    path('tasks/search', task.get_task_by_title_or_description, name='search_tasks'),
    path('category/<int:id_category>/tasks', task.get_tasks_by_category, name='all_tasks_by_category'),


    # All categories routes
    path('categories/', task.get_all_categories, name = 'all_categories'),
    path('category/<int:id_category>', task.get_category_by_id, name = 'single_category'),
    path('category/<int:id_category>', task.get_all_categories, name = 'all_categories'),
]
