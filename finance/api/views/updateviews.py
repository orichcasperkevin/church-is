from rest_framework.response import Response
from rest_framework.views import APIView
# import models
from finance.models import PendingConfirmation
from finance.api.serializers import OfferingSerializer,TitheSerializer

class ConfirmPayment(APIView):
    '''
        confirm Payment
    '''

    def get(self, request, pending_confirmation_id):
        data = {}
        pending_confirmation = PendingConfirmation.objects.get(id=pending_confirmation_id)
        confirmed = pending_confirmation.confirmPayment()
        if (pending_confirmation.type == "O"):
            data = OfferingSerializer(confirmed, many=True).data
        else:
            data = TitheSerializer(confirmed, many=True).data
        return Response(data)
