from django.db import models

# Create your models here.
class Category(models.Model):
    category_name = models.CharField(max_length=40)
    category_priority = models.PositiveIntegerField(default=5)

    def __str__(self) -> str:
        return self.category_name

class Task(models.Model):
    task_title = models.CharField(max_length=150)
    task_description = models.TextField(null=True, blank=True)
    created_at = models.DateField(auto_now=True)
    deadline = models.DateField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.task_title