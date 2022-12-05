from rest_framework import viewsets
from django.shortcuts import get_object_or_404
from .serializers import PostSerializer
from blog.models import Post
from rest_framework.permissions import IsAuthenticated,BasePermission, SAFE_METHODS, AllowAny
from rest_framework.response import Response

class PostUserPermission(BasePermission):
    message = 'This operation is restricted only to author'

    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        else:
            return obj.author == request.user

class PostList(viewsets.ViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Post.postobjects.all()

    def list(self, request):
        serializer_class = PostSerializer(self.queryset, many=True)
        return Response(serializer_class.data)

    def retrieve(self, request, pk=None):
        post = get_object_or_404(self.queryset, pk=pk)
        serializer_class = PostSerializer(post)
        return Response(serializer_class.data)


# class PostList(generics.ListCreateAPIView):
#     permission_classes = [AllowAny]
#     queryset = Post.postobjects.all()
#     serializer_class = PostSerializer
    

# class PostDetail(generics.RetrieveUpdateDestroyAPIView,PostUserPermission):
#     permission_classes = [AllowAny]
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer
