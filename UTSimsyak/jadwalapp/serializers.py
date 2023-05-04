from jadwalapp.models import Jadwal
from rest_framework import serializers

class JadwalImsakSerializer(serializers.ModelSerializer):
    class Meta:
        model = Jadwal
        fields = ['id', 'tanggal', 'imsyak', 'subuh', 'terbit', 'duha', 'zuhur', 'asar', 'magrib','isya' ]