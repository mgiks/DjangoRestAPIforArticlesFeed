from rest_framework import serializers
from .models import Article

class WriterListSerializer(serializers.ModelSerializer):
    #Чтобы поле не показывалось в serializerе
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    
    class Meta:
        model = Article
        fields = ["id", "title", "body", "private", "timestamp", "updated", "user"]

