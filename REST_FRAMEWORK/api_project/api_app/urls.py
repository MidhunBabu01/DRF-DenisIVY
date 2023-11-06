from django.urls import path
from api_app import views


app_name = 'api_app'

urlpatterns = [
    path('task-list-api',views.task_list,name='task_list'),
    path('task-details-api/<int:task_id>/',views.task_details,name='task_details'),
    path('task-create-api',views.task_create,name='task_create'),
    path('task-update-api/<int:update_id>/',views.task_update,name='task_update'),
    path('task-delete-api/<int:delete_id>/',views.task_delete,name='task_delete'),
    
]
