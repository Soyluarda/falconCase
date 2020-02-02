from django.urls import path,include
from .views import *

urlpatterns = [
    path('list/',UserListAPIView.as_view()),
    path('char/add',AddCharAPIView.as_view()),


]
