from django.urls import path
from .views import CreateUser, BlacklistTokenUpdateView
app_name = 'users'

urlpatterns = [
    path('register/',CreateUser.as_view(),name='create_user'),
    path('logout/blacklist/', BlacklistTokenUpdateView.as_view(),
         name='blacklist')
]
