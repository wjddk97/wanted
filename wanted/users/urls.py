from django.urls import path

from users.views import SiupView, LoginView


urlpatterns = [
    path('/signup', SiupView.as_view()),
    path('/login', LoginView.as_view())
]