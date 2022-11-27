from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from .serializers import RegistrationUserSerializer
from rest_framework_simplejwt.tokens import RefreshToken

class CreateUser(APIView):
    permission_classes = [AllowAny]

    def post(self,request):
        print(request.data)
        create_user_serializer = RegistrationUserSerializer(data = request.data)
        if create_user_serializer.is_valid():
            user = create_user_serializer.save()
            return Response(create_user_serializer.data,status=status.HTTP_201_CREATED)
        print('bal')
        return Response(create_user_serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class BlacklistTokenUpdateView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        try:
            refresh_token = request.data["refresh_token"]
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response(status=status.HTTP_205_RESET_CONTENT)
        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST)
