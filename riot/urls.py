from django.urls import path
from .views import *

urlpatterns = [
    path('index',index),
    path('api/ranked-data/', requestRankedDataAPI.as_view()),
    path('api/lor-ranked-data/', lorRankedAPI.as_view()),
    path('api/shard-data/', shardDataAPI.as_view()),

]
