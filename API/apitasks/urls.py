from django.urls import path
from .views import TaskView


urlpatterns = [
    path('tasks/', TaskView.as_view(), name='tasks_list'),
    path('tasks/<int:id>', TaskView.as_view(), name='tasks_process')
]