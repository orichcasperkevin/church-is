from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
# import models
from finance.models import *
from member.models import Member
from finance.api.serializers import OfferingSerializer,TitheSerializer

def updateModelField(model_object,field,data):
    if data:
        #get model object field.
        attr = getattr(model_object,field)
        #change it to something else.
        setattr(model_object,field,data)
        #save.
        model_object.save()
    else:
        pass


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

class UpdateOffering(APIView):
    '''
        patch:
        update member offering
    '''
    def patch(self, request):
        offering_id = request.data.get("offering_id")
        try:
            member  = Member.objects.get(member__id=request.data.get('member_id')) or None
        except Member.DoesNotExist:
            member = None
        try:
            offering = Offering.objects.get(id=offering_id)

            updateModelField(offering,'type_id',request.data.get('type_id'))
            updateModelField(offering,'amount',request.data.get('amount'))
            updateModelField(offering,'date',request.data.get('date'))
            updateModelField(offering,'member',member)
            updateModelField(offering,'name_if_not_member',request.data.get('non_member_name'))
            updateModelField(offering,'service_id',request.data.get('service_id'))
            updateModelField(offering,'narration',request.data.get('narration'))

            return Response(status=status.HTTP_204_NO_CONTENT)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)

class UpdateTithe(APIView):
    '''
        patch:
        update member tithe
    '''
    def patch(self, request):
        tithe_id = request.data.get("tithe_id")
        try:
            member  = Member.objects.get(member__id=request.data.get('member_id')) or None
        except Member.DoesNotExist:
            member = None
        try:
            tithe = Tithe.objects.get(id=tithe_id)

            updateModelField(tithe,'amount',request.data.get('amount'))
            updateModelField(tithe,'date',request.data.get('date'))
            updateModelField(tithe,'member',member)
            updateModelField(tithe,'narration',request.data.get('narration'))

            return Response(status=status.HTTP_204_NO_CONTENT)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)


class UpdateIncome(APIView):
    '''
        patch:
        update Income.
    '''
    def patch(self, request):
        income_id = request.data.get("income_id")
        try:
            income = Income.objects.get(id=income_id)

            updateModelField(income,'type_id',request.data.get('type_id'))
            updateModelField(income,'amount',request.data.get('amount'))
            updateModelField(income,'date',request.data.get('date'))
            updateModelField(income,'narration',request.data.get('narration'))

            return Response(status=status.HTTP_204_NO_CONTENT)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)

class UpdateExpenditure(APIView):
    '''
        patch:
        update expenditure
    '''
    def patch(self, request):
        expenditure_id = request.data.get("expenditure_id")
        try:
            expenditure = Income.objects.get(id=expenditure_id)

            updateModelField(expenditure,'type_id',request.data.get('type_id'))
            updateModelField(expenditure,'amount',request.data.get('amount'))
            updateModelField(expenditure,'date',request.data.get('date'))
            updateModelField(expenditure,'narration',request.data.get('narration'))

            return Response(status=status.HTTP_204_NO_CONTENT)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)
