from rest_framework import serializers
from member.api.serializers import MemberSerializer
from church_social.models import *

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ('name',)

    def create(self, validated_data):
        name = validated_data.pop('name')
        tag = Tag.objects.get_or_create(name=name)
        return tag[0]

class DiscussionSerializer(serializers.ModelSerializer):
    creator = MemberSerializer()
    class Meta:
        model = Discussion
        fields = ('id','topic','description','creation_time','creator','open','tags',)
        depth = 2

    def create(self,validated_data):
        creator = {}
        creator_data = validated_data.pop('creator')
        creator = Member.objects.get(id=creator_data['id'])

        discussion = Discussion.objects.create(creator=creator, **validated_data)
        return discussion

class DiscussionContributionSerializer(serializers.ModelSerializer):
    discussion = DiscussionSerializer()
    contributor = MemberSerializer()
    class Meta:
        model = DiscussionContribution
        fields = ('id','discussion','contributor','contribution','creation_time','votes_up','votes_down',)
        depth = 1
        extra_kwargs = {'id': {'read_only': False}}

class TagMembershipSerializer(serializers.ModelSerializer):
    tag = TagSerializer()
    discussion = DiscussionSerializer()
    class Meta:
        model = TagMembership
        depth = 1
        fields = ('discussion', 'tag',)

    def create(self, validated_data):
        tag= {}
        tag_data = validated_data.pop('tag')
        tag = Tag.objects.get(**tag_data)

        discussion = {}
        discussion_data = validated_data.pop('discussion')
        discussion = Discussion.objects.get(topic=discussion_data['topic'])

        tag_membership = TagMembership.objects.create(discussion=discussion,tag=tag)
        return tag_membership

class DiscussionReactionSerializer(serializers.ModelSerializer):
    discussion = DiscussionSerializer()
    reaction_by = MemberSerializer()
    class Meta:
        model = DiscussionReaction
        fields = ('discussion','recomendation','reaction','reaction_by',)

    def create(self,validated_data):
        discussion = {}
        discussion_data = validated_data.pop('discussion')
        discussion = Discussion.objects.get(topic=discussion_data['topic'])

        member = {}
        member_data = validated_data.pop('reaction_by')
        reaction_by = Member.objects.get(id=member_data['id'])

        reaction = DiscussionReaction.objects.create(discussion=discussion,reaction_by=reaction_by,**validated_data)
        return reaction

class AddContributionToDiscussionSerializer(serializers.ModelSerializer):
    discussion = DiscussionSerializer()
    contributor = MemberSerializer()
    class Meta:
        model = DiscussionContribution
        fields = ('discussion','contributor','contribution',)

    def create(self,validated_data):
        discussion = {}
        discussion_data = validated_data.pop('discussion')
        discussion = Discussion.objects.get(topic=discussion_data['topic'])

        member = {}
        member_data = validated_data.pop('contributor')
        contributor = Member.objects.get(id=member_data['id'])

        contribution = DiscussionContribution.objects.create(discussion=discussion,contributor=contributor,**validated_data)
        return contribution

class AddCommentToContributionSerializer(serializers.ModelSerializer):
    contribution = DiscussionContributionSerializer()
    commentor = MemberSerializer()
    class Meta:
        model = CommentToContribution
        fields = ('contribution','comment','commentor',)

    def create(self, validated_data):
        member = {}
        member_data = validated_data.pop('commentor')
        commentor = Member.objects.get(id=member_data['id'])

        contribution = {}
        contribution_data = validated_data.pop('contribution')
        contribution = DiscussionContribution.objects.get(id=contribution_data['id'])

        comment = CommentToContribution.objects.create(contribution=contribution,commentor=commentor,**validated_data)
        return comment



class ChannelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Channel
        fields = ('name', 'description', 'open',)

class ChannelParticipantSerializer(serializers.ModelSerializer):
    channel = ChannelSerializer()
    class Meta:
        model = ChannelParticipant
        fields = ('channel',)
        depth = 1

class ChannelMessageSerializer(serializers.ModelSerializer):
    sender = MemberSerializer()
    channel = ChannelSerializer()
    class Meta:
        model = ChannelMessage
        fields = ('id','channel','sender','message','type','time_stamp',)
        depth = 2
    def create(self,validated_data):
        member = {}
        member_data = validated_data.pop('sender')
        sender = Member.objects.get(id=member_data['id'])

        channel = {}
        channel_data = validated_data.pop("channel")
        channel = Channel.objects.get(**channel_data)

        message = ChannelMessage.objects.create(sender=sender,channel=channel,**validated_data)
        return message


class PeerToPeerMessageSerializer(serializers.ModelSerializer):
    sender = MemberSerializer()
    receiver = MemberSerializer()
    class Meta:
        model = PeerToPeerMessage
        fields = ('id','sender','receiver','message','time_stamp',)

    def create(self,validated_data):
        sender = {}
        sender_data = validated_data.pop('sender')
        sender = Member.objects.get(id=sender_data['id'])

        receiver = {}
        receiver_data = validated_data.pop('receiver')
        receiver = Member.objects.get(id=receiver_data['id'])

        message = PeerToPeerMessage.objects.create(sender=sender,receiver=receiver,**validated_data)
        return message
