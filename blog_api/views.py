from rest_framework import generics
from .serializers import PostSerializer
from blog.models import Post
from rest_framework.permissions import IsAuthenticated,BasePermission, SAFE_METHODS

class PostUserPermission(BasePermission):
    message = 'This operation is restricted only to author'

    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        else:
            return obj.author == request.user

class PostList(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Post.postobjects.all()
    serializer_class = PostSerializer
    

class PostDetail(generics.RetrieveUpdateDestroyAPIView,PostUserPermission):
    permission_classes = [PostUserPermission]
    queryset = Post.objects.all()
    serializer_class = PostSerializer
