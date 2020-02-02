from django.shortcuts import render
import requests
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from rest_framework.response import Response
from django.core.exceptions import SuspiciousOperation
from .models import *





def index(request):
    return render(request,'index.html')


class requestRankedDataAPI(APIView):
    permission_classes = [AllowAny]
    def post(self, request):
        api_key = request.POST.get('api_key')
        region = request.POST.get('region')
        url = "https://" + str(region) + ".api.riotgames.com/lol/platform/v3/champion-rotations?api_key=" +str(api_key)
        try:
            response = requests.get(url)
        except requests.exceptions.ConnectionError:
            raise SuspiciousOperation("Something wrong, check your request please.")
        return Response(response.json())


class lorRankedAPI(APIView):
    permission_classes = [AllowAny]
    def post(self, request):
        api_key = request.POST.get('api_key')
        region = request.POST.get('region')
        url = "https://" + str(region) + ".api.riotgames.com/lor/ranked/v1/leaderboards?api_key=" +str(api_key)
        try:
            response = requests.get(url)
        except requests.exceptions.ConnectionError:
                raise SuspiciousOperation("Something wrong, check your request please.")


        _region = Region.objects.get_or_create(name=region)
        try:
            players = response.json()['players']
        except:
            raise SuspiciousOperation('Data format wrong.')
        for player in players:
            lor_user = LorRanked.objects.get_or_create(name=player['name'])
            _region[0].lor_ranked.add(lor_user[0])
            if lor_user[0].rank != player['rank']:
                lor_user[0].rank = player['rank']
                lor_user[0].save()

        return Response(response.json())


class shardDataAPI(APIView):
    permission_classes = [AllowAny]
    def post(self, request):
        api_key = request.POST.get('api_key')
        region = request.POST.get('region')
        url = "https://" + str(region) + ".api.riotgames.com/lol/status/v3/shard-data"
        headers = {'Content-Type': 'application/json', 'X-Riot-Token': api_key}
        try:
            r = requests.get(url, headers=headers)
        except requests.exceptions.ConnectionError:
            raise SuspiciousOperation("Something wrong, check your request please.")
        return Response(r.json())








