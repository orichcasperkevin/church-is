from rest_framework import serializers
from dailyVerses.models import (Verse)

class VerseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Verse
        fields = ('id','text','verse','day')
        extra_kwargs = {'id': {'read_only': False}}