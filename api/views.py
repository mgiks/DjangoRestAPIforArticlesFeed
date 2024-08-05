from rest_framework.views import APIView
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions 
from .models import Article
from .serializers import WriterListSerializer
from .permissions import IsAuthor, IsSubscriber

#View автора/подписчика с показом всех статей(публичных/закрытых)
class AuthenticatedApiView(APIView):
    authentication_classes = [BasicAuthentication, SessionAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    
    def get(self, request, *args, **kwargs):
        Articles = Article.objects.all()
        serializer = WriterListSerializer(Articles, context={'request': request}, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
#View незарегестрированного пользователя с показом только публичных статей
class AnonymousUserApiView(APIView):
    def get(self, request, *args, **kwargs):
        Articles = Article.objects.filter(private=False)
        serializer = WriterListSerializer(Articles, context={'request': request}, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

#View автора с показом всех его статей(публичных/закрытых)
class WriterApiView(ListCreateAPIView):
    authentication_classes = [BasicAuthentication, SessionAuthentication]
    permission_classes = [IsAuthor]
    
    queryset = Article.objects.all()
    serializer_class = WriterListSerializer
    
    #Кнопка для удаления всего контента автора
    def delete(self, request, *args, **kwargs):
        Article.objects.all().delete()
        return Response({"res": "No Article object exists yet"}, status=status.HTTP_204_NO_CONTENT)

    def get(self, request, *args, **kwargs):
        Articles = Article.objects.filter(user = request.user.id)
        serializer = WriterListSerializer(Articles, context={'request': request}, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
#View автора с показом всех его закрытых статей  
class WriterPrivateApiView(ListCreateAPIView):
    authentication_classes = [BasicAuthentication, SessionAuthentication]
    permission_classes = [IsAuthor]
    
    queryset = Article.objects.all()
    serializer_class = WriterListSerializer
    
    #Кнопка для удаления всех закрытых статей автора
    def delete(self, request, *args, **kwargs):
        Article.objects.all().filter(private=True).delete()
        return Response({"res": "No Article object exists yet"}, status=status.HTTP_204_NO_CONTENT)

    def get(self, request, *args, **kwargs):
        Articles = Article.objects.filter(user = request.user.id,private=True)
        serializer = WriterListSerializer(Articles, context={'request': request}, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
#View автора с показом всех его открытых статей
class WriterPublicApiView(ListCreateAPIView):
    authentication_classes = [BasicAuthentication, SessionAuthentication]
    permission_classes = [IsAuthor]
    
    queryset = Article.objects.all().filter(private=False)
    serializer_class = WriterListSerializer
    
    #Кнопка для удаления всех публичных статей автора
    def delete(self, request, *args, **kwargs):
        Article.objects.all().filter(private=False).delete()
        return Response({"res": "No Article object exists yet"}, status=status.HTTP_204_NO_CONTENT)

    def get(self, request, *args, **kwargs):
        Articles = Article.objects.filter(user = request.user.id, private=False)
        serializer = WriterListSerializer(Articles, context={'request': request}, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

#View автора с показом определенной статьи по id этой статьи
class WriterDetailApiView(RetrieveUpdateDestroyAPIView):
    authentication_classes = [BasicAuthentication, SessionAuthentication]
    permission_classes = [IsAuthor]

    queryset = Article.objects.all()
    serializer_class = WriterListSerializer
    lookup_field = "pk"
    
    def get(self, request, pk, *args, **kwargs):
        Articles = Article.objects.filter(user = request.user.id, id=pk)
        serializer = WriterListSerializer(Articles, context={'request': request}, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
#View подписчика с показом всех закрытых статей  
class SubscriberPrivateApiView(APIView):
    authentication_classes = [BasicAuthentication, SessionAuthentication]
    permission_classes = [IsSubscriber]
    
    def get(self, request, *args, **kwargs):
        Articles = Article.objects.all().filter(private=True)
        serializer = WriterListSerializer(Articles, context={'request': request}, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
#View подписчика с показом всех публичных статей  
class SubscriberPublicApiView(APIView):
    authentication_classes = [BasicAuthentication, SessionAuthentication]
    permission_classes = [IsSubscriber]
    
    def get(self, request, *args, **kwargs):
        Articles = Article.objects.all().filter(private=False)
        serializer = WriterListSerializer(Articles, context={'request': request}, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
            

    
    
