from rest_framework.views import APIView
from rest_framework.generics import CreateAPIView
from .models import User
from .serializers import UserSerializer
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from api.permissions import IsAuthor
from rest_framework.response import Response
from rest_framework import status

class UserApiView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

#View всех пользователей доступный только для авторов
class AllUsersApiView(APIView):
    authentication_classes = [BasicAuthentication, SessionAuthentication]
    permission_classes = [IsAuthor]
    
    def get(self, request, *args, **kwargs):
        Users = User.objects.all()
        serializer = UserSerializer(Users, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)