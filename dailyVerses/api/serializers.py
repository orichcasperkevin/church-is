from rest_framework import serializers

from dailyVerses.models import (Verse)


class VerseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Verse
        fields = ('id', 'text', 'verse', 'lesson', 'by', 'day')
        extra_kwargs = {'id': {'read_only': False}}
        depth = 2
