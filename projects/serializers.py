from rest_framework import serializers

from member.api.serializers import MemberSerializer
from projects.models import (Project,Pledge)

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ('id','church_group','name','start','stop','description','required_amount','raised_amount','remaining_amount','percentage_funded')
        depth = 1
        extra_kwargs = {'id': {'read_only': True}}

class PledgeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pledge
        fields = ('project','member', 'name','phone','')
        depth = 2
        extra_kwargs = {'id': {'read_only': True}}
