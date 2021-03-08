from django.utils.html import format_html
from django.utils.translation import gettext_lazy as _
from geopy.geocoders import Nominatim


def get_headshot_image(image):
    '''returns the image displayedin admin inlines overview'''
    if image:
        return format_html(f'<a href="{image.url}" target="_blank">'
                           f'<img src="{image.url}" style="max-height:500px;"/>'  # noqa
                           f'</a>')
    else:
        return _("No Image Found")


def get_image_format(image):
    '''returns the image displayed in admin model overview'''
    if image:
        return format_html(
            f'<img src="{image.url}" style="max-width:100px;" />')
    else:
        return _("No Image Found")


def get_coordinates(address):
    """returns the coordinates to a given address.
            possible methods:
                .address
                .latitude
                .longitude
                .point
                .raw
                .altitude
    """
    geolocator = Nominatim(user_agent="realestate-tornode")
    location = geolocator.geocode(address)
    return location
