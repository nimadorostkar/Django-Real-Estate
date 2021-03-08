from django.db import models
from django.utils.translation import gettext_lazy as _


# ============================================================= >> LISTING FILE
class ListingFile(models.Model):
    listing = models.ForeignKey('listings.Listing', default=None,
                                on_delete=models.DO_NOTHING,
                                verbose_name=_("Listing"))
    name = models.CharField(max_length=255,
                            verbose_name=_("Name"))
    short_description = models.CharField(max_length=255,
                                         verbose_name=_("Short description"))
    file = models.FileField(default=None, upload_to='listings/files/',
                            verbose_name=_("File"))
    created = models.DateTimeField(auto_now_add=True,
                                   verbose_name=_("Created"))
    updated = models.DateTimeField(auto_now=True, null=True,
                                   verbose_name=_("Updated"))
    for_customer = models.BooleanField(default=True,
                                       verbose_name=_("For customers"))

    def __str__(self):
        return (f"{self.listing.title}")

    def get_listing_title(self):
        return self.listing.title
    get_listing_title.short_description = _("Listing")
