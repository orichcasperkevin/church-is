
import random
from datetime import timedelta

from decouple import config
from django.utils import timezone
from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from tenant_schemas.utils import schema_context

from .forms import *
from member.models import *
from groups.models import *
from projects.models import *
from .models import Client,ClientDetail,ChurchSMSCredentials,ChurchSiteVisit

from .website.content import WebContent

SMS_QUOTA = 0.2
DEFAULT_DATE = "2012-01-01"
STARTER_PASSWORD = "changeMe"
DEMO_MEMBERS = [['Daniel','Dambuki','M','M'],['Mercy','Masika','F','M'],['Dorothy','Nyambura','F','S'],['David','Masai','M','S'],['Paul','Mwai','M','M'],
                ['Timothy','Resty','M','S'],['Christina','Shusho','F','M'],['Ann','Mutai','F','M'],['Nickson','Korir','M','S']]

DEMO_GROUPS = [['men','all the men of the church',['Daniel','David','Paul','Timothy','Nickson'],None],
               ['women','all women of the church',['Mercy','Dorothy','Christina','Ann'],None],
               ['deacons','deacons of the church',['Daniel','Dorothy','Nickson'],'leaders'],
               ['ministers','church ministers',['Ann','Daniel','David','Mercy'],'leaders']]

DEMO_GROUP_OF_GROUPS = [['leaders']]
DEMO_PROJECTS = [['church construction','construction of the new church',300000],['new anvil church software','down payment for a new software',3500],['new furniture','buying pews for the main church hall',4000000]]

def setup_demo_members():
    for data in DEMO_MEMBERS:
        username = data[0].lower() + data[1].lower()
        user = User(first_name = data[0], username=username, last_name = data[1], email=username + '@example.com')
        user.save()
        user_id = user.id

        member = Member.objects.create(member_id = user_id, gender=data[2])
        MemberContact.objects.create(member=member, phone = '0713111882')
        MemberMaritalStatus.objects.create(member=member, status = data[3])

def set_up_demo_group_of_groups():
    for data in DEMO_GROUP_OF_GROUPS:
        GroupOfChurchGroups.objects.create(name=data[0],description='a folder')

def set_up_demo_groups():
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
                ChurchGroupMembership.objects.create(church_group=church_group,member=member,role=role)

def set_up_demo_projects():
    for data in DEMO_PROJECTS:
            project = Project.objects.create(name=data[0],description=data[1],start='2020-01-01',
                                             stop='2021-01-01',required_amount=data[2])
            #setup contribution and pledges
            for data2 in DEMO_MEMBERS:
                member = Member.objects.get(member__first_name=data2[0])
                Contribution.objects.create(project=project,member=member,recorded_by=member,
                                            amount=random.choice(range(10000)))
                pledge = Pledge.objects.create(project=project,member=member,recorded_by=member,
                                               date='2019-06-06',amount=random.choice(range(10000)))
                PledgePayment.objects.create(pledge=pledge,payment_amount=random.choice(range(1000)),
                                            payment_recorded_by=member)

def set_up_demo_database(first_name,last_name,email,demo_name):
    #inside the demo schema
    with schema_context(demo_name):
        #create first member
        username = first_name.lower() + last_name.lower()
        user = User(first_name=first_name, username=username, last_name=last_name, email=email)
        user.set_password(STARTER_PASSWORD)
        user.save()
        user_id = user.id

        member = Member.objects.create(member_id = user_id)
        setup_demo_members()
        set_up_demo_group_of_groups()
        set_up_demo_groups()
        set_up_demo_projects()

        change_password_url = '/change-password/' + username + '/'+ demo_name + '/'
        return change_password_url

def set_up_client_database(first_name,last_name,phone_number,email,formated_name_of_church):
    with schema_context(formated_name_of_church):
        #inside the clents schema. create first memberself
        username = first_name.lower() + last_name.lower()
        user = User(first_name=first_name, username=username, last_name=last_name, email=email)
        user.set_password(STARTER_PASSWORD)
        user.save()
        user_id = user.id

        member = Member.objects.create(member_id = user_id)
        MemberContact.objects.create(member=member, phone = phone_number)
        Role.objects.create(role='member',is_group_role=True)
        Role.objects.create(role='group admin',is_group_role=True)
        change_password_url = '/change-password/' + username + '/'+ formated_name_of_church + '/'
        return change_password_url

'''
    anvil website and clients' website
'''
def index(request):
    if (request.tenant.schema_name == 'public'
        or request.tenant.schema_name == 'Public'):
        return render(request, 'index.html')

    if request.tenant.schema_name == 'methodistpublic':
        return render(request, 'methodistindex.html')

    else:
        website_content = WebContent(request.tenant.schema_name).content
        ChurchSiteVisit.objects.create(church=Client.objects.get(schema_name=request.tenant.schema_name))
        return render(request,'clientWebsite/index.html',{'website_content':website_content})

'''
    get anvil registration
'''
def get_anvil(request):
    with schema_context('public'):
        if request.method == 'POST':
            get_anvil_form = GetAnvilForm(request.POST)
            #try using the get anvil form
            if get_anvil_form.is_valid():
                #peronal info
                first_name = get_anvil_form.cleaned_data['first_name'].strip()
                last_name = get_anvil_form.cleaned_data['last_name'].strip()
                phone_number = get_anvil_form.cleaned_data['phone_number'].strip()
                ID_number = get_anvil_form.cleaned_data['ID_number'].strip()
                email = get_anvil_form.cleaned_data['email'].strip()

                #church detai;
                name_of_church = get_anvil_form.cleaned_data['name_of_church']
                city_or_town = get_anvil_form.cleaned_data['city_or_town']
                road_or_street = get_anvil_form.cleaned_data['road_or_street']
                location_description = get_anvil_form.cleaned_data['location_description']
                website = get_anvil_form.cleaned_data['website']

                formated_name_of_church = ('').join(name_of_church.split(' '))
                formated_name_of_church = formated_name_of_church.replace('.','')
                domain_url = formated_name_of_church + "." + request.get_host().split(':')[0]

                tenant = Client(domain_url=domain_url, schema_name=formated_name_of_church,
                             name = name_of_church,paid_until=DEFAULT_DATE, on_trial=False)
                tenant.save()
                ClientDetail.objects.create(client=tenant,first_name=first_name,last_name=last_name,
                                         ID_number=ID_number,phone_number=phone_number,city_or_town=city_or_town,
                                         road_or_street=road_or_street,location_description=location_description,
                                         website=website)
                redirect_url = set_up_client_database(first_name,last_name,phone_number,email,formated_name_of_church)
                return redirect(redirect_url)
        else:
            get_anvil_form = GetAnvilForm()
        return render(request, 'getAnvil.html', {'get_anvil_form':get_anvil_form})

def get_demo(request):
    with schema_context('public'):
        if request.method == 'POST':
            demo_form = TryDemoForm(request.POST)
            #try using the get anvil form

            if demo_form.is_valid():
                    first_name = demo_form.cleaned_data['first_name'].strip()
                    last_name = demo_form.cleaned_data['last_name'].strip()
                    email = demo_form.cleaned_data['email'].strip()
                    phone_number = demo_form.cleaned_data['phone_number'].strip()
                    #demo name
                    demo_name = "demo" + str(random.choice(range(10000000)))
                    #domain_url
                    domain_url = demo_name +"."+ request.get_host().split(':')[0]
                    name = first_name +" "+ last_name + " " + email + " " +phone_number
                    tenant = Client(domain_url=domain_url, schema_name=demo_name,
                                     name=name,paid_until=DEFAULT_DATE,on_trial=True)
                    tenant.save()
                    # setup client details
                    ClientDetail.objects.create(client=tenant,first_name=first_name,last_name=last_name,phone_number=phone_number)
                    redirect_url = set_up_demo_database(first_name,last_name,email,demo_name)
                    return redirect(redirect_url)
        else:
            demo_form = TryDemoForm()
        return render(request, 'getDemo.html', {'demo_form':demo_form})

def change_password(request, username, church_name):
    if request.method == 'POST':
        change_password_form = ChangePasswordForm(request.POST)
        if change_password_form.is_valid():
            new_username = change_password_form.cleaned_data['username']
            new_password = change_password_form.cleaned_data['confirm_password']
            with schema_context(church_name):
                member = Member.objects.get(member__username=username)
                user = User.objects.get(id=member.member.id)
                try:
                    user.username = new_username
                    user.set_password(new_password)
                    user.save()
                except:
                    return redirect('password_error/')
                else:
                    return redirect(config('ADMIN_APP_URL'))
    else:
        change_password_form = ChangePasswordForm()
    client = Client.objects.get(schema_name=church_name)
    church_code = client.church_code
    return render (request , 'changePassword.html', {'change_password_form':change_password_form,'username':username,'church_code':church_code})

def password_fail(request):
    return render(request, 'passwordFail.html')

@login_required
def anvil_admin(request):
    clients = ClientDetail.objects.filter(client__on_trial = False)
    demos = ClientDetail.objects.filter(client__on_trial = True)
    return render(request, 'anvilAdmin.html' ,{'clients':clients,'demos':demos},)

@login_required
def add_credit(request,client_id):
    client = Client.objects.get(id=client_id)
    if request.method == 'POST':
        add_credit_form = AddCreditForm(request.POST)
        if add_credit_form.is_valid():
            #adding credit amount.
            added_amount = add_credit_form.cleaned_data['amount']
            client_detail  = ClientDetail.objects.get(client_id=client_id)
            initial_amount = client_detail.credit
            new_amount = initial_amount + added_amount
            client_detail.credit = new_amount
            client_detail.save()

            #update paid until
            price_per_month = client_detail.tier['price_per_month']
            price_per_day = (price_per_month / 30)
            number_of_days =  int(float(client_detail.credit) / price_per_day)
            client.paid_until = timezone.now() + timedelta(days=number_of_days)
            client.save()
            return redirect('anvilAdmin')
    else:
        add_credit_form = AddCreditForm()
    return render (request , 'addCredit.html', {'add_credit_form':add_credit_form,'client':client})

@login_required
def edit_SMS_credentials(request,client_id):
    client = Client.objects.get(id=client_id)
    if request.method == 'POST':
        edit_SMS_credentials_form = EditSMSCredentialsForm(request.POST)
        if edit_SMS_credentials_form.is_valid():
            credentials  = ChurchSMSCredentials.objects.get_or_create(church_id=client_id)[0]
            credentials.at_username = edit_SMS_credentials_form.cleaned_data['at_username']
            credentials.at_api_key = edit_SMS_credentials_form.cleaned_data['at_api_key']
            credentials.at_sender_id = edit_SMS_credentials_form.cleaned_data['at_sender_id']

            credentials.at_mpesa_acc_no = edit_SMS_credentials_form.cleaned_data['at_mpesa_acc_no']
            credentials.at_mpesa_paybill = edit_SMS_credentials_form.cleaned_data['at_mpesa_paybill']
            credentials.save()
            return redirect('anvilAdmin')
    else:
        edit_SMS_credentials_form = EditSMSCredentialsForm()
    return render (request , 'editCredentials.html', {'edit_SMS_credentials_form':edit_SMS_credentials_form,'client':client})

@login_required
def delete_account(request,client_id):
    client = Client.objects.get(id=client_id)
    client.delete()
    return redirect('anvilAdmin')
