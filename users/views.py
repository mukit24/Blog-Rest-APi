from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from .serializers import RegistrationUserSerializer

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
