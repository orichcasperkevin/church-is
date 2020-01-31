import csv
import datetime

from django.db.models import Sum,Avg
from django.http import HttpResponse

from finance.models import *
def date_format(date_str):
    date = date_str.split("-")
    year = date[0]
    month = date[1]
    day = date[2]

    return {"year":year,"month":month,"day":day}

def some_view(request):
    # Create the HttpResponse object with the appropriate CSV header.
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="somefilename.csv"'

    writer = csv.writer(response)
    writer.writerow(['First row', 'Foo', 'Bar', 'Baz'])
    writer.writerow(['Second row', 'A', 'B', 'C', '"Testing"', "Here's a quote"])

    return response

def get_tithes_csv(request,date):
    filename = "tithes_for_" + date
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename=filename'

    #date = datetime.datetime(date)
    writer = csv.writer(response)
    date = date_format(date)
    for tithe in Tithe.objects.filter(date__month=date["month"],date__year=date["year"]):
        names = tithe.member.member.first_name + " " + tithe.member.member.last_name
        amount = tithe.amount
        tithe_date = tithe.date
        narration = tithe.narration

        writer.writerow([names, amount, tithe_date, narration])
    total_tithes = Tithe.objects.filter(date__month=date["month"],date__year=date["year"]).aggregate(Sum('amount'))['amount__sum']
    avg_tithes = Tithe.objects.filter(date__month=date["month"],date__year=date["year"]).aggregate(Avg('amount'))['amount__avg']
    writer.writerow(["TOTAL", total_tithes])
    writer.writerow(["AVERAGE", round(avg_tithes,2)])

    return response
