from django.db import models
from datetime import datetime
from django.conf import settings
from django.utils.translation import ugettext_lazy as _



class Contact(models.Model):
    listing = models.ForeignKey('listings.Listing',
                                on_delete=models.DO_NOTHING,
                                verbose_name=_("Listing"))
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.PROTECT, verbose_name=_("User"))
    phone = models.CharField(max_length=100, verbose_name=_("Phone"))
    message = models.TextField(blank=True, verbose_name=_("Message"))
    contact_date = models.DateTimeField(default=datetime.now, blank=True,
                                        verbose_name=_("Contact date"))
    can_access_documents = models.BooleanField(default=False,
                                               verbose_name=_("Docs access"))

    class Meta:
        ordering = ['-contact_date']

    def __str__(self):
        return f"{self.listing} - {self.user}"

    def get_full_name(self):
        return f"{self.user.first_name} {self.user.last_name}"
    get_full_name.short_description = _("Client")

    def get_email(self):
        return f"{self.user.email}"
    get_email.short_description = _("Email")


    
class ChatMessage(models.Model):
    contact = models.ForeignKey(Contact, on_delete=models.PROTECT,
                                verbose_name=_("Contact listing"))
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.PROTECT, verbose_name=_("User"))
    message = models.TextField(null=True, blank=False)
    timestamp = models.DateTimeField(default=datetime.now, blank=True,
                                     verbose_name=_("Date and iime"))

    class Meta:
        ordering = ['-timestamp']

    def __str__(self):
        return f"{self.contact} - {self.user} - {self.message}"
