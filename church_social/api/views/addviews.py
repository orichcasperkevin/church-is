from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from church_social.api.serializers import TagSerializer,DiscussionSerializer,TagMembershipSerializer
from church_social.models import Tag,TagMembership,Discussion

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

class AddTagMembership(APIView):
    '''
        add a discussion to a tag
    '''
    def post(self, request):

        name = request.data.get("name")
        queryset = Tag.objects.filter(name=name)
        data = []
        for data in queryset:
            data = data
        serializer = TagSerializer(data)
        tag = serializer.data

        discussion_id = request.data.get("discussion_id")
        queryset = Discussion.objects.filter(discussion_id=discussion_id)
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
