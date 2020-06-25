from django.urls import path, include
from .views import employee_list, employee_create, employee_update, employee_delete

urlpatterns = [
    path("", employee_list, name="home"),
    path("create/", employee_create, name="employee_create"),
    path("update/<int:pk>/", employee_update, name="employee_update"),
    path("delete/<int:pk>/", employee_delete, name="employee_delete"),
]