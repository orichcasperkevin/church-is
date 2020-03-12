import csv
import datetime

from django.db.models import Sum,Avg
from django.http import HttpResponse

from finance.models import *
from services.models import ServiceType

def date_format(date_str):
    date = date_str.split("-")
    year = date[0]
    month = date[1]
    day = date[2]

    return {"year":year,"month":month,"day":day}

def get_tithes_csv(request,date):
    filename = "tithes_for_" + date
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename=filename'

    #date = datetime.datetime(date)
    writer = csv.writer(response)
    date = date_format(date)
    writer.writerow(["names", "amount", "tithe_date", "narration"])
    for tithe in Tithe.objects.filter(date__month=date["month"],date__year=date["year"]):
        names = "anonymous"
        if tithe.member:
            names = tithe.member.member.first_name + " " + tithe.member.member.last_name
        if tithe.group:
            names = tithe.group.name
        if tithe.service:
            names = tithe.service.type.name + "(" + str(tithe.service.date.strftime(" %a %d %b, %Y")) + ")"

        amount = tithe.amount
        tithe_date = tithe.date.strftime(" %a %d %b, %Y")
        narration = tithe.narration

        writer.writerow([names, amount, tithe_date, narration])
    total_tithes = Tithe.objects.filter(date__month=date["month"],date__year=date["year"]).aggregate(Sum('amount'))['amount__sum'] or 0
    avg_tithes = Tithe.objects.filter(date__month=date["month"],date__year=date["year"]).aggregate(Avg('amount'))['amount__avg'] or 0
    writer.writerow(["TOTAL", total_tithes])
    writer.writerow(["AVERAGE", round(avg_tithes,2)])

    return response


def get_member_offering_csv(request,date):
    filename = "member_offerings_for" + date
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename=filename'

    #date = datetime.datetime(date)
    writer = csv.writer(response)
    date = date_format(date)
    for type in OfferingType.objects.all():
        writer.writerow([str(type).upper()])
        writer.writerow(["offering_type","name","amount","offering_date","narration"])

        for offering in Offering.objects.filter(type_id=type.id,member__isnull=False,date__month=date["month"],date__year=date["year"]):
            offering_type = str(type)
            name = offering.member.member.first_name + " " + offering.member.member.last_name
            offering_date = offering.date.strftime(" %a %d %b, %Y")
            amount = offering.amount
            narration = offering.narration

            writer.writerow([offering_type,name,amount,offering_date,narration])

        total_in_offering =  Offering.objects.filter(type_id=type.id,member__isnull=False,date__month=date["month"],date__year=date["year"]).aggregate(Sum('amount'))['amount__sum'] or 0
        avg_offering =  Offering.objects.filter(type_id=type.id,member__isnull=False,date__month=date["month"],date__year=date["year"]).aggregate(Avg('amount'))['amount__avg'] or 0

        writer.writerow(["","TOTAL", total_in_offering])
        writer.writerow(["","AVERAGE", round(avg_offering,2)])
        writer.writerow([])

    return response

def get_service_offering_csv(request,date):
    filename = "service_offerings_for" + date
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename=filename'

    #date = datetime.datetime(date)
    writer = csv.writer(response)
    date = date_format(date)
    for type in ServiceType.objects.all():
        writer.writerow([str(type).upper()])
        writer.writerow(["service","amount","date","narration"])

        for offering in Offering.objects.filter(service__type_id=type.id,service__isnull=False,date__month=date["month"],date__year=date["year"]):
            service_type = str(type)
            amount = offering.amount
            offering_date = offering.date.strftime(" %a %d %b, %Y")
            narration = offering.narration

            writer.writerow([service_type,amount,offering_date,narration])

        total_in_offering =  Offering.objects.filter(service__type_id=type.id,service__isnull=False,date__month=date["month"],date__year=date["year"]).aggregate(Sum('amount'))['amount__sum'] or 0
        avg_offering =  Offering.objects.filter(service__type_id=type.id,service__isnull=False,date__month=date["month"],date__year=date["year"]).aggregate(Avg('amount'))['amount__avg'] or 0

        writer.writerow(["TOTAL", total_in_offering])
        writer.writerow(["AVERAGE", round(avg_offering,2)])
        writer.writerow([])

    return response

def get_income_csv(request,date):
    filename = "income_for" + date
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename=filename'

    #date = datetime.datetime(date)
    writer = csv.writer(response)
    date = date_format(date)
    for type in IncomeType.objects.all():
        writer.writerow([str(type).upper()])
        writer.writerow(["type","amount","date","narration"])

        for income in Income.objects.filter(type_id=type.id,date__month=date["month"],date__year=date["year"]):
            income_type = str(type)
            amount = income.amount
            income_date = income.date.strftime(" %a %d %b, %Y")
            narration = income.narration

            writer.writerow([income_type,amount,income_date,narration])

        total_income =  Income.objects.filter(type_id=type.id,date__month=date["month"],date__year=date["year"]).aggregate(Sum('amount'))['amount__sum'] or 0
        avg_income =  Income.objects.filter(type_id=type.id,date__month=date["month"],date__year=date["year"]).aggregate(Avg('amount'))['amount__avg'] or 0

        writer.writerow(["TOTAL", total_income])
        writer.writerow(["AVERAGE", round(avg_income,2)])
        writer.writerow([])

    return response

def get_expenditure_csv(request,date):
    filename = "expenditure_for" + date
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename=filename'

    #date = datetime.datetime(date)
    writer = csv.writer(response)
    date = date_format(date)
    for type in ExpenditureType.objects.all():
        writer.writerow([str(type).upper()])
        writer.writerow(["type","amount","date","narration"])

        for expenditure in Expenditure.objects.filter(type_id=type.id,date__month=date["month"],date__year=date["year"]):
            expenditure_type = str(type)
            amount = expenditure.amount
            income_date = expenditure.date.strftime(" %a %d %b, %Y")
            narration = expenditure.narration

            writer.writerow([expenditure_type,amount,income_date,narration])

        total_expenditure =  Expenditure.objects.filter(type_id=type.id,date__month=date["month"],date__year=date["year"]).aggregate(Sum('amount'))['amount__sum'] or 0
        avg_expenditure =  Expenditure.objects.filter(type_id=type.id,date__month=date["month"],date__year=date["year"]).aggregate(Avg('amount'))['amount__avg'] or 0

        writer.writerow(["TOTAL", total_expenditure])
        writer.writerow(["AVERAGE", round(avg_expenditure,2)])
        writer.writerow([])

    return response
