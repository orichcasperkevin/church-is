from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from Clients.api.serializers import ChurchStatementSerializer,ChurchCoreValueSerializer
                                    ChurchPeriodicThemeSerializer,ChurchAboutSerializer
from Clients.models import ChurchStatement,ChurchCoreValue,ChurchPeriodicTheme

class AddChurchStatement(APIView):
    '''
        post:
        add church statements
    '''
    def post(self, request):

        church_id = request.data.get("church_id")
        mission = request.data.get("mission")
        vision = request.data.get("vision")

        data = {'church': church_id, 'mission': mission, 'vision': vision}
        serializer = ChurchStatementSerializer(data=data)

        if serializer.is_valid():
            created = serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class AddAboutChurchAPIView):
    '''
        post:
        add church about.
    '''
    def post(self, request):

        church_id = request.data.get("church_id")
        about = request.data.get("about")

        data = {'church': church_id, 'about': about}
        serializer = ChurchAboutSerializer(data=data)

        if serializer.is_valid():
            created = serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class AddChurchCoreValue(APIView):
    '''
        post:
        add church core value
    '''
    def post(self, request):

        church_id = request.data.get("church_id")
        value = request.data.get("value")

        data = {'church': church_id, 'value': value}
        serializer = ChurchCoreValueSerializer(data=data)

        if serializer.is_valid():
            created = serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class AddChurchPeriodicTheme(APIView):
    '''
        post:
        add church periodic theme.
    '''
    def post(self, request):

        church_id = request.data.get("church_id")
        theme = request.data.get("theme")
        description = request.data.get("description")
        start = request.data.get("start")
        end = request.data.get("end")

        data = {
                'church': church_id, 'theme': theme, 'description':description,
                'start':start, 'end':end
                }
        serializer = ChurchPeriodicThemeSerializer(data=data)

        if serializer.is_valid():
            created = serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
