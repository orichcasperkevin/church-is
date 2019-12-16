import random

from django.shortcuts import render
from django.contrib.auth.models import User
from tenant_schemas.utils import schema_context

from .forms import TryDemoForm,getAnvilForm
from member.models import *
from groups.models import *
from projects.models import *

from .models import Client

STARTER_PASSWORD = "changeMe"
DEMO_MEMBERS = [['Daniel','Dambuki','M','M'],['Mercy','Masika','F','M'],['Dorothy','Nyambura','F','S'],['David','Masai','M','S'],['Paul','Mwai','M','M'],
                ['Timothy','Resty','S','M'],['Christina','Shusho','F','M'],['Ann','Mutai','F','M'],['Nickson','Korir','M','S']]

DEMO_GROUPS = [['men','all the men of the church',['Daniel','David','Paul','Timothy','Nickson'],None],
               ['women','all women of the church',['Mercy','Dorothy','Christina','Ann'],None],
               ['deacons','deacons of the church',['Daniel','Dorothy','Nickson'],'leaders'],
               ['ministers','church ministers',['Ann','Daniel','David','Mercy'],'leaders']]

DEMO_GROUP_OF_GROUPS = [['leaders']]
DEMO_PROJECTS = [['church construction',300000],['new anvil church software',3500],['new furniture',4000000]]

def setupDemoMembers():
    for data in DEMO_MEMBERS:
        username = data[0].lower() + data[1].lower()
        user = User(first_name = data[0], username=username, last_name = data[1], email=username + '@example.com')
        user.save()
        user_id = user.id

        member = Member.objects.create(member_id = user_id, gender=data[2])
        MemberContact.objects.create(member=member, phone = '07##########')
        MemberMaritalStatus.objects.create(member=member, status = data[3])

def setUpDemoGroupOfGroups():
    for data in DEMO_GROUP_OF_GROUPS:
        GroupOfChurchGroups.objects.create(name=data[0],description='a folder')

def setUpDemoGroups():
    for data in DEMO_GROUPS:
        if data[3]:
            folder = GroupOfChurchGroups.objects.get(name = 'leaders')
            church_group = ChurchGroup.objects.create(group=folder,name=data[0],description=data[1])
            for name in data[2]:
                member = Member.objects.get(member__first_name=name)
                role = Role.objects.get_or_create(role='member')[0]
                ChurchGroupMembership.objects.create(church_group=church_group,member=member,role=role)

        else:
            church_group = ChurchGroup.objects.create(name=data[0],description=data[1])
            for name in data[2]:
                member = Member.objects.get(member__first_name=name)
                role = Role.objects.get_or_create(role='member')[0]
                print(role)
                ChurchGroupMembership.objects.create(church_group=church_group,member=member,role=role)



def setupDemoProjects():
    DEMO_PROJECTS = [['church construction','construction of the new church',300000],['new anvil church software','down payment for a new software',3500],['new furniture','buying pews for the main church hall',4000000]]
    for data in DEMO_PROJECTS:
            project = Project.objects.create(name=data[0],description=data[1],start='2020-01-01',stop='2021-01-01',required_amount=data[2])
            #setup contribution and pledges
            for data2 in DEMO_MEMBERS:
                member = Member.objects.get(member__first_name=data2[0])
                Contribution.objects.create(project=project,member=member,recorded_by=member,amount=random.choice(range(10000)))
                pledge = Pledge.objects.create(project=project,member=member,recorded_by=member,date='2019-06-06',amount=random.choice(range(10000)))
                PledgePayment.objects.create(pledge=pledge,payment_amount=random.choice(range(1000)),payment_recorded_by=member)



def setupDemoDatabase(first_name,last_name,email,demo_name):
    #inside the demo schema
    with schema_context(demo_name):
        #create first member
        username = first_name.lower() + last_name.lower()
        user = User(first_name=first_name, username=username, last_name=last_name, email=email)
        user.set_password(STARTER_PASSWORD)
        user.save()
        user_id = user.id

        member = Member.objects.create(member_id = user_id)
        setupDemoMembers()
        setUpDemoGroupOfGroups()
        setUpDemoGroups()
        setupDemoProjects()



def index(request):
    if request.method == 'POST':
        demo_form = TryDemoForm(request.POST)
        get_anvil_form = getAnvilForm(request.POST)
        try:
            #try using the get anvil form
            if getAnvilForm.is_valid(request.POST):
                print("ouhs")
        except:
            #use the demo form
            if demo_form.is_valid():
                first_name = demo_form.cleaned_data['first_name']
                last_name = demo_form.cleaned_data['last_name']
                email = demo_form.cleaned_data['email']
                #demo name
                demo_name = "demo" + str(random.choice(range(10000000)))
                #domain_url
                domain_url = demo_name +"."+ request.get_host().split(':')[0]
                print(domain_url)
                tenant = Client(domain_url=domain_url, schema_name=demo_name,
                                name=first_name,paid_until='2014-12-05',on_trial=True)
                tenant.save()
                setupDemoDatabase(first_name,last_name,email,demo_name)


    else:
        demo_form = TryDemoForm()
        get_anvil_form = getAnvilForm()
    return render(request, 'index.html', {'demo_form':demo_form ,'get_anvil_form':get_anvil_form})
