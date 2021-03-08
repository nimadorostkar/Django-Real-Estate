from django.db import models
from datetime import datetime, date
from django.utils.translation import gettext_lazy as _
from uuid import uuid4
from core.libs.core_libs import (get_headshot_image, get_image_format,
                                 get_coordinates)


def listing_dir_path(instance, filename):
    ext = filename.split('.')[-1]
    if instance.pk:
        filename = '{}.{}'.format(instance.pk, ext)
    else:
        # set filename as random string
        filename = '{}.{}'.format(uuid4().hex, ext)
    return (f'listings/{filename}')


# ============================================================= >> LISTING TYPE
class ListingType(models.Model):
    """ListingTypes designate basic appartment, maisonette, loft, houses, etc.
    """

    name = models.CharField(max_length=100, blank=False, null=False,
                            unique=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.name}'

    def get_nr_listings(self):
        return 5


LISTING_CHOICE = {
    (_("R"), _("Rent")),
    (_("S"), _("Sell")),
}


# ================================================================== >> LISTING
class Listing(models.Model):
    listing_type = models.ForeignKey(ListingType, on_delete=models.PROTECT,
                                     verbose_name=_("Listing type"))
    realtor = models.ForeignKey('accounts.Realtor',
                                on_delete=models.DO_NOTHING,
                                verbose_name=_("Realtor"))
    title = models.CharField(max_length=50, verbose_name=_("Title"))
    address = models.ForeignKey('core.Address', on_delete=models.PROTECT,
                                default=1, null=True,
                                verbose_name=_("Address"))
    description = models.TextField(blank=True,
                                   verbose_name=_("Description"))
    price = models.DecimalField(max_digits=20, decimal_places=2,
                                verbose_name=_("Price"))
    ceiling_height = models.FloatField(blank=True, null=True,
                                       verbose_name=_("Ceiling height"))
    bedrooms = models.PositiveIntegerField(verbose_name=_("Bedrooms"))
    bathrooms = models.PositiveIntegerField(verbose_name=_("Bathrooms"))
    garage = models.IntegerField(default=0,
                                 verbose_name=_("Garage"))
    sqft                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      = models.FloatField(verbose_name=_("m²"))
    lot_size = models.FloatField(verbose_name=_("Lot size"))  # Grunstückgröße
    image = models.ImageField(upload_to=listing_dir_path,
                              verbose_name=_("Image"))
    listing_for = models.CharField(max_length=5, choices=LISTING_CHOICE,
                                   default="S", verbose_name=_("Listing for"))
    protected = models.BooleanField(default=False,
                                    verbose_name=_("Monument Protected"))
    is_published = models.BooleanField(default=True, verbose_name=_("Online"))
    free_from = models.DateField(default=datetime.now, blank=True,
                                 verbose_name=_("Free from"))
    created = models.DateTimeField(auto_now_add=True, null=True,
                                   verbose_name=_("Created"))
    updated = models.DateTimeField(auto_now=True, null=True,
                                   verbose_name=_("Updated"))

    def __str__(self):
        return self.title

    def free_date(self):
        if self.free_from <= date.today():
            return _("Immediatly")
        else:
            return self.free_from

    def get_total_rooms(self):
        return self.bedrooms + self.bedrooms
    get_total_rooms.short_description = _("# Rooms")

    def get_address(self):
        return (f"{self.address.street} {self.address.hn}, {self.address.city}"
                f", {self.address.state.country.shortcut}")
    get_address.short_description = _("Address")

    def get_price(self):
        return f"{self.price}€"
    get_price.short_description = _("Price")

    def get_sqft(self):
        return _("{} m²".format(self.sqft))
    get_sqft.short_description = _("m²")

    def get_ceiling_height(self):
        return f"{self.ceiling_height} m"
    get_ceiling_height.short_description = _("Ceiling Height")

    def get_image(self):
        return get_image_format(self.image)

    get_image.short_description = _('Image')

    def headshot_image(self):
        return get_headshot_image(self.image)

    headshot_image.short_description = _('Preview')

    def get_images(self):
        '''returns nr of inline images'''
        return self.listingimage_set.count() + 1 if self.image else \
            self.listingimage_set.count()

    get_images.short_description = _('# Images')

    def get_nr_files(self):
        '''returns nr of inline files'''
        return self.listingfile_set.count()
    get_nr_files.short_description = _('# Files')

    def get_coordinates(self):
        return get_coordinates(f"{self.address.street} {self.address.hn} "
                               f"{self.address.zipcode} {self.address.city}")


# ============================================================ >> LISTING IMAGE
class ListingImage(models.Model):
    listing = models.ForeignKey(Listing, default=None,
                                on_delete=models.DO_NOTHING,
                                verbose_name=_("Listing"))
    image = models.ImageField(default=None, upload_to=listing_dir_path,
                              null=True, blank=True,
                              verbose_name=_("Image"))
    short_description = models.CharField(max_length=255,
                                         verbose_name=_("Short description"))
    created = models.DateTimeField(auto_now_add=True,
                                   verbose_name=_("Created"))

    def __str__(self):
        return (f"{self.listing.title}")

    def get_image(self):
        return get_image_format(self.image)

    get_image.short_description = _("Image")

    def headshot_image(self):
        return get_headshot_image(self.image)

    headshot_image.short_description = _("Preview")

    def get_listing_title(self):
        return self.listing.title

    get_listing_title.short_description = _("Listing")


# ============================================================= >> LISTING FILE
class ListingToCustomer(models.Model):
    listing = models.ForeignKey(Listing, default=None,
                                on_delete=models.DO_NOTHING)
