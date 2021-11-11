from django.urls import path
from user.views import *
urlpatterns = [
    path('register/',RegisterView.as_view(),name='register'),
    path('login/',LoginView.as_view(),name='login'),
    path('logout/',LogoutView.as_view(),name='logout'),
    path('test_middleware/',test_middleware),
    path('imagecode/',ImagecodeView.as_view(),name='imagecode'),
    path('smscode/',SmscodeView.as_view(),name = 'smscode'),
]



