from django.db import models

class Article(models.Model):
    title = models.CharField(max_length = 180)
    body = models.TextField()
    private = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add = True, auto_now = False)
    updated = models.DateTimeField(auto_now = True, blank = True)
    user = models.ForeignKey('users.User', on_delete = models.CASCADE, blank = True)

    def __str__(self):
        return self.task

