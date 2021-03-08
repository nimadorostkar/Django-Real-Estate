from django import forms
from .models import Address
from django.utils.translation import ugettext_lazy as _


class BasicFormStyle(forms.ModelForm):
    """define the base and the form name"""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for key, field in self.fields.items():
            field.widget.attrs['class'] = "form-control"


class ProfileUpdateForm(BasicFormStyle):

    class Meta():
        model = Address
        fields = ['street', 'hn', 'zipcode', 'city', 'last_login']
        widgets = {
            'street': forms.TextInput(attrs={'placeholder': _("Street"),
                                             'name': 'street',
                                             'type': 'text',
                                             'aria-required': 'true',
                                             'minlength': '2'}),
            'hn': forms.TextInput(attrs={'placeholder': _("House Number"),
                                         'name': 'hn',
                                         'type': 'text',
                                         'aria-required': 'true'}),
            'zipcode': forms.TextInput(attrs={'placeholder': _("Zipcode"),
                                              'name': 'zipcode',
                                              'type': 'number',
                                              'aria-required': 'true',
                                              'minlength': '5'}),
            'city': forms.TextInput(attrs={'placeholder': _("City"),
                                           'name': 'city',
                                           'type': 'text',
                                           'aria-required': 'true',
                                           'minlength': '2'}),

        }
