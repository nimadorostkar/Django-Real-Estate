from django import template
from contacts.models import Contact
from listings.models import Listing
from crum import get_current_user


register = template.Library()


@register.filter(name='listing_exists')
def listing_exists(listing_id):
    """Returns true if user has already made an inquiry"""
    user = get_current_user()
    try:
        contact = Contact.objects.get(listing=listing_id, user=user.id)
        return contact.id
    except Exception:
        return False


@register.filter(name='get_nr_docs')
def get_nr_docs(listing_id):
    """Returns true if user has already made an inquiry"""
    listing = Listing.objects.get(id=listing_id)
    return listing.listingfile_set.filter(for_customer=True).count()
