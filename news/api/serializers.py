from rest_framework import serializers

from news.models import (News, )


class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = ('heading','church_group','article',
                  'date', 'author', 'website')
        depth = 2
        extra_kwargs = {'id': {'read_only': True}}
