from rest_framework import serializers
from .models import *

class MusicianSerializer(serializers.ModelSerializer):
    class Meta:
        model = Musician
        fields = ('id', 'first_name', 'last_name', 'instrument', 'album_set')

class AlbumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Album
        fields = '__all__'