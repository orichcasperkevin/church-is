from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from church_social.api.serializers import (TagSerializer,DiscussionSerializer,TagMembershipSerializer,
        DiscussionReactionSerializer,AddContributionToDiscussionSerializer)
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

class AddReactionToDiscussion(APIView):
    '''
        add a reaction to a discussion
    '''
    def post(self, request):
        reaction = request.data.get("reaction")
        reactor_id = request.data.get("reactor_id")
        discussion_id = request.data.get("discussion_id")

        discussion_id = request.data.get("discussion_id")
        queryset = Discussion.objects.filter(id=discussion_id)
        data = []
        for data in queryset:
            data = data
        serializer = DiscussionSerializer(data)
        discussion = serializer.data

        queryset = Member.objects.filter(id=reactor_id)
        reactor = []
        for reactor in queryset:
            reactor = reactor
        serializer = MemberSerializer(reactor)
        reactor = serializer.data

        data = {'reaction':reaction,'discussion':discussion,'reaction_by':reactor}

        serializer = DiscussionReactionSerializer(data=data)
        if serializer.is_valid():
            created = serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class AddContributionToDiscussion(APIView):
    def post(self,request):
        discussion_id = request.data.get("discussion_id")
        contributor_id = request.data.get("contributor_id")
        contribution = request.data.get("contribution")

        queryset = Discussion.objects.filter(id=discussion_id)
        data = []
        for data in queryset:
            data = data
        serializer = DiscussionSerializer(data)
        discussion = serializer.data

        queryset = Member.objects.filter(id=contributor_id)        
        contributor = []
        for contributor in queryset:
            contributor = contributor
        serializer = MemberSerializer(contributor)
        contributor = serializer.data

        data = {'discussion':discussion,'contributor':contributor,'contribution':contribution}
        serializer = AddContributionToDiscussionSerializer(data=data)

        if serializer.is_valid():
            created = serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
