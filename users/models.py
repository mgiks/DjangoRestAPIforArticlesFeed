from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models

class UserManager(BaseUserManager):
    
    def create_user(self, email: str, password: str = None, is_staff=False, is_superuser=False):
        if not email:
            raise ValueError("User must have an email")
        if not password:
            raise ValueError("User must have a password")

        user = self.model(email=self.normalize_email(email))
        user.set_password(password)
        user.is_active = True
        user.is_staff = is_staff
        user.is_superuser = is_superuser
        user.save()
        
        return user
    
    def create_superuser(self, email: str, password: str):
        user = self.create_user(
            email=email,
            password=password,
            is_staff=True,
            is_superuser=True,
        )
        user.save()
        
        return user

class User(AbstractUser):
    #Роли для зарегестрированных пользователей
    STATUS = (
        ('writer', 'writer'),
        ('subscriber', 'subscriber')
    )
    
    email = models.EmailField(unique=True)
    status = models.CharField(max_length=100, choices=STATUS, default='subscriber')
    username = None
    
    objects = UserManager()
    
    #Замена логина на электронную почту
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []