from django.db import models
from django.utils.translation import gettext_lazy as _





# ================================================================== >> COUNTRY
class Country(models.Model):
    """Country Model."""

    name = models.CharField(
        max_length=150, null=False, blank=False, unique=True)

    shortcut = models.CharField(
        max_length=3, null=False, blank=False, verbose_name="ISO 3166-α2")

    class Meta:
        verbose_name = _("Country")
        verbose_name_plural = _("Countries")

    def __str__(self):
        return f'{self.name}'



# ==================================================================== >> STATE
class State(models.Model):
    """State Model.
    Example:
        country_id      1 - Germany
        name            Berlin
    """

    country = models.ForeignKey(Country, null=False, on_delete=models.CASCADE,
                                verbose_name=_("Country"))
    name = models.CharField(max_length=150, blank=False, null=False,
                            verbose_name=_("Country"))
    shortcut = models.CharField(
        max_length=6, null=False, blank=False, verbose_name="ISO 3166-2")

    class Meta:
        unique_together = ('country', 'shortcut')
        verbose_name = _("State")
        verbose_name_plural = _("States")

    def __str__(self):
        return (f"{self.name} - {self.country.name}")



# ================================================================== >> ADDRESS
class Address(models.Model):
    """Address Model."""
    street = models.CharField(max_length=150, blank=False, null=False,
                              verbose_name=_("Street"))
    hn = models.CharField(max_length=15, blank=False, null=False,
                          verbose_name=_("House number"))
    zipcode = models.CharField(max_length=5, blank=False, null=False,
                               verbose_name=_("Zipcode"))
    city = models.CharField(max_length=100, blank=False, null=False,
                            verbose_name=_("City"))
    state = models.ForeignKey(
        State, blank=False, null=False, on_delete=models.CASCADE,
        verbose_name=_("State"))


    class Meta:
        unique_together = ('street', 'hn', 'zipcode')
        verbose_name_plural = _("Addresses")

    def __str__(self):
        return (f"{self.street} {self.hn}, {self.city}"
                f" - {self.state.country.shortcut}")

    def get_listings(self):
        return self.street
