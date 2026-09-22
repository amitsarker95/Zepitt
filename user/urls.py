from django.urls import path
from .views import UserCreateView, UsersListView

urlpatterns = [
    path('lists/', UsersListView.as_view(), name='lists-user'),
    path('create/', UserCreateView.as_view(), name='create-user'),
]