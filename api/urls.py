from django.urls import path
from . import views
from users.views import AllUsersApiView
urlpatterns = [
    path('', views.AnonymousUserApiView.as_view()),
    path('view_all/', views.AuthenticatedApiView.as_view()),
    path('subscriber/private', views.SubscriberPrivateApiView.as_view()),
    path('subscriber/public', views.SubscriberPublicApiView.as_view()),
    path('writer/', views.WriterApiView.as_view()),
    path('writer/private', views.WriterPrivateApiView.as_view()),
    path('writer/public', views.WriterPublicApiView.as_view()),
    path('writer/users', AllUsersApiView.as_view()),
    path('writer/<int:pk>/', views.WriterDetailApiView.as_view()),
]