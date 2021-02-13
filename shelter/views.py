from django.shortcuts import render,get_object_or_404,HttpResponse
from .models import Listening,Quickcontact,AgentContact
from agents.models import Agent
from  .locations_data import locations
from .forms import QuickContactForm
# Create your views here.

def index(request):
    homes = Listening.objects.all()[:6]
    agents = Agent.objects.all()[:4]
    
    return render(request,'shelter/index.html',{'homes':homes,'agents':agents})


def propertiesList(request):

    if 'increment' not in request.session :
        #declare empty variable 
        counter = 0 
        request.session['increment'] = 0
    
    request.session['increment'] += 6
    counter = request.session['increment']
    
    homes = Listening.objects.all()[:counter]
    return render(request,'shelter/properties_list.html',{'homes':homes})

def propertyDetail(request,slug):
    sidebar_homes = Listening.objects.all()[:3]
    home = get_object_or_404(Listening,slug=slug,available=True)
    return render(request,'shelter/property_detail.html',{'home':home,'sidebar_homes':sidebar_homes})

def contact(request):
    return render(request,'shelter/contact.html')


def searchResult(request):
    #location
    if 'location' in request.GET:
        location = request.GET['location']
        if location:
            query_list = Listening.objects.filter(location__iexact=location)
    # keyword
    if 'keyword' in request.GET:
        keyword = request.GET['keyword']
        if keyword:
            query_list = Listening.objects.filter(description__icontains=keyword) 
    #bedrooms
    if 'bedrooms' in request.GET:

        bedrooms = request.GET['bedrooms']
        if bedrooms:
            query_list = Listening.objects.filter(bedrooms__lte=bedrooms)    

    #bathdrooms
    if 'bathrooms' in request.GET:

        bathrooms = request.GET['bathrooms']
        if bathrooms:
            query_list = Listening.objects.filter(bathrooms__lte=bathrooms) 

    #price
    if 'price' in request.GET:
        price = request.GET['price']
        if price:
            strprice = str(price)
            remove_dollar = int(strprice[1:5])
            if remove_dollar:
                query_list = Listening.objects.filter(price__lte=remove_dollar)  

    return render(request,'shelter/search.html',{'query_list':query_list}) 

def Services(request):
    return render(request,'shelter/services.html')

def Quick_Contact(request):
    return_response = "Thank you your message has been received"
    if request.method == 'POST':
        form = QuickContactForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            saveform = Quickcontact.objects.create(email=cd['email'],textarea=cd['textarea'])
        return HttpResponse(return_response)


def UserAgentContact(request):
    return_response = "Thank you Agent Will contact you"
    if request.method == 'POST':
        agent_name = request.POST['agentname']
        user_name = request.POST['name']
        user_email = request.POST['email']
        user_subject = request.POST['textarea']
        agentcontact = AgentContact.objects.create(agentname=agent_name,user_name=user_name,
                                            user_email=user_email,user_subject=user_subject)
        return HttpResponse(return_response)

