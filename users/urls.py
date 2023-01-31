from django.urls import path

from users.views import new_user, list_user

urlpatterns = [
    path('new_user/', new_user),
    path('list_user/', list_user)
]