import random

from django.shortcuts import render
from .forms import TryDemoForm,getAnvilForm
from .models import Client

def index(request):
    if request.method == 'POST':
        demo_form = TryDemoForm(request.POST)
        get_anvil_form = getAnvilForm(request.POST)
        try:
            if getAnvilForm.is_valid(request.POST):
                print("ouhs")
        except:
            if demo_form.is_valid():
                name = demo_form.cleaned_data['name']
                email = demo_form.cleaned_data['email']
                #demo name
                demo_name = "demo" + str(random.choice(range(10000000)))
                print(demo_name)
                #domain_url
                domain_url = demo_name +"."+ request.get_host().split(':')[0]
                print(domain_url)

                tenant = Client(domain_url=domain_url, schema_name=demo_name,
                                name=name,paid_until='2014-12-05',on_trial=True)
                tenant.save() # migrate_schemas automatically called, your tenant is ready to be used!

    else:
        demo_form = TryDemoForm()
        get_anvil_form = getAnvilForm()
    return render(request, 'index.html', {'demo_form':demo_form ,'get_anvil_form':get_anvil_form})
