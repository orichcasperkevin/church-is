import json
from tenant_schemas.utils import schema_context
from Clients.models import *


from news.models import News
from news.api.serializers import NewsSerializer

from events.models import Event
from events.api.serializers import EventSerializer

from services.models import ServiceType,ServiceItem
from services.api.serializers import ServiceTypeSerializer,ServiceItemSerializer


class WebContent():
    def __init__(self,schema):
        self.schema = schema
        self.content = {
                        #contents of the church website
                        "logo_url":None,
                        "name_of_church": None,
                        "number_of_members": 0,
                        "location": {"town":'',"road":'',"description":''},
                        "mission":None,
                        "vission":None,
                        "core_values":None,
                        "theme":{"theme":None,"description":None,"start":None,"end":None},
                        "news":None,
                        "events": None,
                        "service_types":None
                        }

        self.get_church_detail()
        self.get_church_logo()
        self.get_church_content()
        self.get_news()
        self.get_events()
        self.get_service_types()

    def get_church_detail(self):
        '''
            get church name location etc
        '''
        self.content["name_of_church"]  = Client.objects.get(schema_name=self.schema).name
        client_detail = ClientDetail.objects.get(client__schema_name=self.schema)

        self.content["location"]["town"] = client_detail.city_or_town
        self.content["location"]["road"] = client_detail.road_or_street
        self.content["location"]["description"] = client_detail.location_description

        self.content["number_of_members"] = client_detail.number_of_members

    def get_church_logo(self):
        try:
            self.content["logo_url"] = ChurchLogo.objects.get(church__schema_name=self.schema).logo
        except ChurchLogo.DoesNotExist:
            pass

    def get_church_content(self):
        '''
            get church preliminary content
        '''
        core_values = []
        for value in ChurchCoreValue.objects.filter(church__schema_name=self.schema):
            core_values.append(value.value)
        self.content["core_values"] = core_values

        theme = ChurchPeriodicTheme.objects.filter(church__schema_name=self.schema)[:1]
        if len(theme):
            self.content["theme"]["theme"] = theme[0].theme
            self.content["theme"]["description"] = theme[0].description
            self.content["theme"]["start"] = theme[0].start
            self.content["theme"]["end"] = theme[0].end


        '''
            mission and vission statements
        '''
        try:
            self.content["mission"] = ChurchStatement.objects.get(church__schema_name=self.schema).mission
            self.content["vission"] = ChurchStatement.objects.get(church__schema_name=self.schema).mission
        except ChurchStatement.DoesNotExist:
            pass


    def get_news(self):
        with schema_context(self.schema):
            news =  News.objects.all()[:10]
            news = NewsSerializer(news,many=True).data
            self.content["news"] = json.loads(json.dumps(news))

    def get_events(self):
        with schema_context(self.schema):
            events = Event.objects.all().order_by('-start_datetime')[:25]
            events = EventSerializer(events,many=True).data
            self.content["events"] = json.loads(json.dumps(events))

    def get_service_types(self):
        with schema_context(self.schema):
            service_types = ServiceType.objects.all()
            service_types = ServiceTypeSerializer(service_types,many=True).data
            self.content["service_types"] =  json.loads(json.dumps(service_types))
