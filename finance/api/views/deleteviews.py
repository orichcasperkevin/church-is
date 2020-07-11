from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

# import models
from finance.models import Tithe, Offering

class deleteEnvelope(APIView):
    '''
        delete an envelope
    '''
    def delete(self, request):
        context = request.data.get("context")
        envelope_ids = request.data.get("envelope_ids")

        for id in envelope_ids:
            try:
                if context == "All":
                    if (id['type'] == "Tithe"):
                        try:
                            tithe = Tithe.objects.get(id=id['id'])
                            tithe.delete()
                        except Tithe.DoesNotExist:
                            pass
                    else:
                        try:
                            offering = Offering.objects.get(id=id['id'])
                            offering.delete()
                        except Offering.DoesNotExist:
                            pass

                if context == "Tithe":
                    try:
                        tithe = Tithe.objects.get(id=id)
                        tithe.delete()
                    except Tithe.DoesNotExist:
                        pass

                if context == "Offering":
                    try:
                        offering = Offering.objects.get(id=id)
                        offering.delete()
                    except Offering.DoesNotExist:
                        pass
            except:
                return Response(status=status.HTTP_400_BAD_REQUEST)
        return Response(status=status.HTTP_204_NO_CONTENT)
