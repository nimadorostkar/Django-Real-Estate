from .locations_data import locations
from .forms import QuickContactForm
# For location
def search_locations(request):
    return {'search_locations': locations }

def quick_contact_form(request):
    return {'quickcontactform': QuickContactForm}
    