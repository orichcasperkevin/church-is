from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from church_social.api.serializers import TagSerializer,DiscussionSerializer,TagMembershipSerializer
from church_social.models import Tag,TagMembership,Discussion
from member.models import Member
from member.api.serializers import MemberSerializer

class AddDiscussion(APIView):
    '''
        add discussion
    '''
    def post(self, request):
        topic = request.data.get("topic")
        description = request.data.get("description")
        creator_id = request.data.get("creator_id")
        open = request.data.get("open")

        queryset = Member.objects.filter(id=creator_id)
        creator = []
        for creator in queryset:
            creator = creator
        serializer = MemberSerializer(creator)
        creator = serializer.data

        data = {'topic':topic,'description':description,'creator':creator,'open':open}

        serializer = DiscussionSerializer(data=data)
        if serializer.is_valid():
            created = serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class AddTag(APIView):
    '''
        add a tag
    '''
    def post(self,request):
        name = request.data.get("name")

        data = {'name': name}
        serializer = TagSerializer(data=data)
        if serializer.is_valid():
            created = serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class AddTagToDiscussion(APIView):
    '''
        add a discussion to a tag
    '''
    def post(self, request):

        name = request.data.get("tag_name")
        queryset = Tag.objects.filter(name=name)
        data = []
        for data in queryset:
            data = data
        serializer = TagSerializer(data)
        tag = serializer.data

        discussion_id = request.data.get("discussion_id")
        queryset = Discussion.objects.filter(id=discussion_id)        
        data = []
        for data in queryset:
            data = data
        serializer = DiscussionSerializer(data)
        discussion = serializer.data

        data = {'tag': tag, 'discussion': discussion}

        serializer = TagMembershipSerializer(data=data)
        if serializer.is_valid():
            created = serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
