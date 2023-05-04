from django.shortcuts import render

from jadwalapp.models import Jadwal
from jadwalapp.serializers import JadwalImsakSerializer
from rest_framework import viewsets

# Create your views here.

class JadwalImsakViewSet(viewsets.ModelViewSet):
    queryset = Jadwal.objects.all()
    serializer_class = JadwalImsakSerializer
