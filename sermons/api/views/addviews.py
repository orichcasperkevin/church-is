from rest_framework import generics,status
from rest_framework.views import APIView
from rest_framework.response import Response

from member.models import Member
from sermons.models import (Sermon)

from member.api.serializers import MemberSerializer
from sermons.api.serializers import SermonSerializer,AddSermonSerializer

class addSermon(APIView):
    '''
        add a sermon.
    '''
    def post(self,request):
        serializer = 1
        preaching_member_id = request.data.get("preaching_member_id")
        if (preaching_member_id != None):
            queryset = Member.objects.filter(member_id = preaching_member_id)
            data = []
            for data in queryset:
                data = data
            serializer = MemberSerializer(data)
            member = serializer.data
        else:
            member = None
            serializer = 2

        title = request.data.get("title")
        slug = request.data.get("slug")
        type = request.data.get("type")
        youtube_video_url = request.data.get("youtube_url")
        date = request.data.get("date")
        preached_by = request.data.get("name_if_not_member")
        website = request.data.get("website")

        data = {'title':title,'slug':slug, 'type':type, 'youtube_video_url':youtube_video_url,
                'date':date, 'preached_by_member':member, 'preached_by':preached_by, 'website':website}
        if (serializer == 1 ):
            serializer = SermonSerializer(data=data)
        else:
            serializer = AddSermonSerializer(data=data)

        if serializer.is_valid():
            created = serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
