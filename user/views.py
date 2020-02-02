from rest_framework.generics import ListAPIView, CreateAPIView
from .models import ExtendedUser
from riot.models import Char
from .serializers import UserSerializer
from riot.serializers import CharSerializer
from rest_framework.response import Response
from django.views.static import serve
from django.core.exceptions import SuspiciousOperation
from django.core.cache import cache
from rest_framework import status
from django.core.cache.backends.base import DEFAULT_TIMEOUT
from django.conf import settings


CACHE_TTL = getattr(settings, 'CACHE_TTL', DEFAULT_TIMEOUT)



class UserListAPIView(ListAPIView):
    queryset = ExtendedUser.objects.all()
    serializer_class = UserSerializer


    def list(self,request,*args,**kwargs):
        if 'user' in cache:
            user = cache.get('user')
            return Response(user, status=status.HTTP_201_CREATED)

        else:
            queryset = self.get_queryset()
            serializer = UserSerializer(queryset, many=True)
            user = serializer.data
            cache.set('user', user, timeout=CACHE_TTL)
            return Response(serializer.data, status=status.HTTP_200_OK)




class AddCharAPIView(CreateAPIView):
    model = Char
    serializer_class = CharSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        user = ExtendedUser.objects.filter(id=self.request.user.id).all()
        if user:
            user.char.add(Char.objects.all().order_by('-id')[0])
        return Response(serializer.data)


def protected_serve(request, path, document_root=None, show_indexes=False):
    return serve(request, path, document_root, show_indexes)