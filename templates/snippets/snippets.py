rom geopy.geocoders import Nominatim

>>> print(location.address)
Flatiron Building, 175, 5th Avenue, Flatiron, New York, NYC, New York, ...
>>> print((location.latitude, location.longitude))
(40.7410861, -73.9896297241625)
>>> print(location.raw)
{'place_id': '9167009604', 'type': 'attraction', ...}


LAAMMEEE 

<QuerySet 
[<Listing: Nice house in balleville>, 
 <Listing: Awesome Flat for the whole family>, 
 <Listing: Pretty Cottage in the nature>, 
 <Listing: Neubauwohnung>, <Listing: Altbauwohnung>]>



def register(request):
	if request.method == "POST":
		form = UserCreationForm(request.POST)
		if form.is_valid():
			user = form.save()
			username = form.cleaned_data.get('username')
			messages.success(request, f"New account created: {username}")
			login(request, user, backend='django.contrib.auth.backends.ModelBackend')
		else:
			messages.error(request,"Account creation failed")

		return redirect("main:homepage")

	form = UserCreationForm()
	return render(request,"register.html", {"form": form})



    
    template_name = "accounts/auth/password_reset.html"
    return render(request, context, template_name)