from django.contrib import admin
from django.urls import path

from todos.views import TodoListView, TodoCreateView, TodoUpdadateView, TodoDeleteView, TodoCompleteView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", TodoListView.as_view(), name="todo_list"),
    path("create", TodoCreateView.as_view(), name="todo_create"),
    path("update/<int:pk>", TodoUpdadateView.as_view(), name="todo_update"),
    path("delete/<int:pk>", TodoDeleteView.as_view(), name="todo_delete"),
    path("complete/<int:pk>", TodoCompleteView.as_view(), name="todo_complete"),
]
