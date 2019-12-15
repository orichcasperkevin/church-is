import random

from django.shortcuts import render
from django.contrib.auth.models import User
from tenant_schemas.utils import schema_context

from .forms import TryDemoForm,getAnvilForm
from member.models import Member
from .models import Client

STARTER_PASSWORD = "changeMe"

def setupDemoDatabase(first_name,last_name,email,demo_name):
    #inside the demo schema
    with schema_context(demo_name):
        #create member
        username = first_name.lower() + last_name.lower()
        print(username)
        user = User(first_name=first_name, username=username, last_name=last_name, email=email)
        user.set_password(STARTER_PASSWORD)
        user.save()
        print(user)
        user_id = user.id

        member = Member.objects.create(member_id = user_id)
        print(member)


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
