from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from Clients.models import ChurchStatement,ChurchCoreValue,ChurchPeriodicTheme,ChurchAbout

def update_model_field(model_object,field,data):
    if data:
        #print(getattr(model_object,field)) #get model object field.(uncomment for debugging purposes)
        setattr(model_object,field,data)#change it to something else.
        model_object.save()#save.
    else:
        pass

class UpdateAboutChurch(APIView):
    '''
        patch:
        update about church.
    '''
    def patch(self, request):
        church_id = request.data.get("church_id")
        about = ChurchAbout.objects.get(church_id=church_id)
    
        try:
            update_model_field(about,'about',request.data.get("about"))

            return Response(status=status.HTTP_204_NO_CONTENT)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)

class UpdateChurchStatement(APIView):
    '''
        patch:
        update church mission and vision statements
    '''
    def patch(self, request):
        church_id = request.data.get("church_id")
        church_statements = ChurchStatement.objects.get(church_id=church_id)
        try:
            update_model_field(church_statements,'mission',request.data.get("mission"))
            update_model_field(church_statements,'vision',request.data.get("vision"))

            return Response(status=status.HTTP_204_NO_CONTENT)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)

class UpdateChurchCoreValue(APIView):
    '''
        patch:
        update church about
    '''
    def patch(self, request):
        church_id = request.data.get("church_id")
        about = ChurchAbout.objects.get(church_id=church_id)
        try:

            update_model_field(about,'about',request.data.get("about"))

            return Response(status=status.HTTP_204_NO_CONTENT)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)


class UpdateChurchCoreValue(APIView):
    '''
        patch:
        update church core value
    '''
    def patch(self, request):
        church_id = request.data.get("church_id")
        value_id = request.data.get("value_id")
        church_value = ChurchCoreValue.objects.get(church_id=church_id,id=value_id)
        try:
            update_model_field(value,'value',request.data.get("value"))

            return Response(status=status.HTTP_204_NO_CONTENT)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)

class UpdateChurchPeriodicTheme(APIView):
    '''
        patch:
        update church periodic theme
    '''
    def patch(self, request):
        church_id = request.data.get("church_id")
        theme_id = request.data.get("theme_id")
        church_theme = ChurchPeriodicTheme.objects.get(church_id=church_id,id=theme_id)
        try:
            update_model_field(church_theme,'theme',request.data.get("theme"))
            update_model_field(church_theme,'description',request.data.get("description"))
            update_model_field(church_theme,'start',request.data.get("start"))
            update_model_field(church_theme,'end',request.data.get("end"))

            return Response(status=status.HTTP_204_NO_CONTENT)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)
