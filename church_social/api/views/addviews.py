from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from church_social.api.serializers import *
from church_social.models import *
from member.models import Member
from member.api.serializers import MemberSerializer

class AddPeerToPeerNewMessage(APIView):
    '''
        add a new message
    '''
    def post(self,request):
        sender_id = request.data.get("sender_id")
        queryset = Member.objects.filter(member_id=sender_id)
        sender = []
        for sender in queryset:
            sender = sender
        serializer = MemberSerializer(sender)
        sender = serializer.data

        receiver_id = request.data.get("receiver_id")
        queryset = Member.objects.filter(member_id=receiver_id)
        receiver = []
        for receiver in queryset:
            receiver = receiver
        serializer = MemberSerializer(receiver)
        receiver = serializer.data

        message = request.data.get("message")

        data = {'sender':sender,'receiver':receiver,'message':message}

        serializer = PeerToPeerMessageSerializer(data=data)
        if serializer.is_valid():
            created = serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class AddPeerToPeerNewMessageBulk(APIView):
    '''
        add a new message
    '''
    def post(self,request):
        sender_id = request.data.get("sender_id")
        sender = Member.objects.get(member_id=sender_id)

        message = request.data.get("message")

        receiver_ids = request.data.get("receiver_ids")
        for id in receiver_ids:
            try:
                receiver = Member.objects.get(id=id)
                PeerToPeerMessage.objects.create(sender=sender,receiver=receiver,message=message)
            except:
                pass

        return Response(["success"], status=status.HTTP_201_CREATED)

class AddChannelNotification(APIView):
    def post(self,request):
        sender_id = request.data.get("sender_id")
        queryset = Member.objects.filter(member_id=sender_id)
        sender = []
        for sender in queryset:
            sender = sender
        serializer = MemberSerializer(sender)
        sender = serializer.data

        group_name = request.data.get("group_name")
        channel_name = '_'.join(group_name.split(' '))
        queryset = Channel.objects.filter(name=channel_name)
        channel = []
        for channel in queryset:
            channel = channel
        serializer = ChannelSerializer(channel)
        channel = serializer.data

        message = request.data.get("message")
        type = "A" #Announcement

        data = {'channel':channel,'sender':sender,'message':message,'type':type}

        print(data)
        serializer = ChannelMessageSerializer(data=data)
        print(serializer.initial)
        if serializer.is_valid():
            created = serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class AddDiscussion(APIView):
    '''
        add discussion
    '''
    def post(self, request):
        topic = request.data.get("topic")
        description = request.data.get("description")
        creator_id = request.data.get("creator_id")
        open = request.data.get("open")

        queryset = Member.objects.filter(member_id=creator_id)
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
        recomendation = request.data.get("recomendation")
        reactor_id = request.data.get("reactor_id")
        discussion_id = request.data.get("discussion_id")

        discussion_id = request.data.get("discussion_id")
        queryset = Discussion.objects.filter(id=discussion_id)
        data = []
        for data in queryset:
            data = data
        serializer = DiscussionSerializer(data)
        discussion = serializer.data

        queryset = Member.objects.filter(member_id=reactor_id)
        reactor = []
        for reactor in queryset:
            reactor = reactor
        serializer = MemberSerializer(reactor)
        reactor = serializer.data

        data = {'reaction':reaction,'recomendation':recomendation,'discussion':discussion,'reaction_by':reactor}

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

        queryset = Member.objects.filter(member_id=contributor_id)
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

class AddCommentToContribution(APIView):
    def post(self, request):
        commentor_id = request.data.get("commentor_id")
        contribution_id = request.data.get("contribution_id")
        comment = request.data.get("comment")

        queryset = DiscussionContribution.objects.filter(id=contribution_id)
        contribution = []
        for contribution in queryset:
            contribution = contribution
        serializer = DiscussionContributionSerializer(contribution)
        contribution = serializer.data

        queryset = Member.objects.filter(member_id=commentor_id)
        commentor = []
        for commentor in queryset:
            commentor = commentor
        serializer = MemberSerializer(commentor)
        commentor = serializer.data

        data = {'commentor':commentor,'contribution':contribution,'comment':comment}
        serializer = AddCommentToContributionSerializer(data=data)

        if serializer.is_valid():
            created = serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
