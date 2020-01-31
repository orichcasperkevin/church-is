import csv
import datetime

from django.db.models import Sum,Avg
from django.http import HttpResponse

from projects.models import *

def date_format(date_str):
    date = date_str.split("-")
    year = date[0]
    month = date[1]
    day = date[2]

    return {"year":year,"month":month,"day":day}

def get_project_stats_as_csv(request,date):
    filename = "projects_overall_stats_for" + date
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename=filename'

    #date = datetime.datetime(date)
    writer = csv.writer(response)
    date = date_format(date)
    for project in Project.objects.filter(start__year=date["year"]):
        name = project.name
        start = project.start
        stop = project.stop
        description = project.description
        required = project.required_amount

        writer.writerow([name,start,stop,stop,description,required])
    total_required = Project.objects.filter(start__year=date["year"]).aggregate(Sum('required_amount'))['required_amount__sum'] or 0
    avg_required = Project.objects.filter(start__year=date["year"]).aggregate(Avg('required_amount'))['required_amount__avg'] or 0
    writer.writerow(["","","","","TOTAL",total_required])
    writer.writerow(["","","","","AVERAGE",round(avg_required,2)])

    return response
