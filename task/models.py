from django.db import models

# Create your models here.

# A task category to describe its type and importance
class Category(models.Model):
    category_name = models.CharField(max_length=40)
    category_priority = models.PositiveIntegerField(default=5)
    
    class Meta: 
        verbose_name_plural = 'Categories'

    def __str__(self) -> str:
        return self.category_name

# Some task to do that has a deadline and a category
class Task(models.Model):
    task_title = models.CharField(max_length=150)
    task_description = models.TextField(null=True, blank=True)
    created_at = models.DateField(auto_now=True)
    deadline = models.DateField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.task_title