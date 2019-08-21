from rest_framework import serializers

from groups.api.serializers import ChurchGroupSerializer
from events.models import Event, EventAttendingGroup, EventAttendedMember

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ('id', 'title', 'description', 'location', 'start', 'end')
        extra_kwargs = {'id': {'read_only': True}}
