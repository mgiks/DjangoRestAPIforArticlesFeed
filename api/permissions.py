from rest_framework import permissions
from rest_framework import serializers

#Кастомные permissions для зарегистрированных пользователей
class IsAuthor(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.is_authenticated and request.user.status == "writer":
            return True
        
class IsSubscriber(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.is_authenticated and request.user.status == "subscriber":
            return True
