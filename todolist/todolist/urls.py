from django.contrib import admin
from django.urls import path
from tasks.views import index, categories, add_category, edit_category, delete_category, tasks, add_task, edit_task
from tasks.views import delete_task


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('categories/', categories, name='categories-list'),
    path('add_category/', add_category, name='add-category'),
    path('edit_category/<int:category_id>', edit_category, name='edit-category'),
    path('delete_category/<int:category_id>', delete_category, name='delete-category'),
    path('tasks/', tasks, name='tasks-list'),
    path('add_task/', add_task, name='add-task'),
    path('edit_task/<int:task_id>', edit_task, name='edit-task'),
    path('delete_task/<int:task_id>', delete_task, name='delete-task')
]
