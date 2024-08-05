from django.urls import path
from . import views

urlpatterns = [
    path('',views.UserApiView.as_view())
]