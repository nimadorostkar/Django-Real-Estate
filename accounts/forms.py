from django import forms
from .models import CustomUser
from django.utils.translation import ugettext_lazy as _


class BasicFormStyle(forms.ModelForm):
    """define the base and the form name"""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for key, field in self.fields.items():
            field.widget.attrs['class'] = "form-control"


class ProfileUpdateForm(BasicFormStyle):

    class Meta():
        model = CustomUser
        fields = ['first_name', 'last_name', 'email', 'phone', 'last_login']
        widgets = {
            'first_name': forms.TextInput(attrs={'placeholder': _("Firstname"),
                                                 'name': 'first_name',
                                                 'type': 'text',
                                                 'aria-required': 'true',
                                                 'minlength': '2'}),
            'last_name': forms.TextInput(attrs={'placeholder': _("Lastname"),
                                                'name': 'last_name',
                                                'type': 'text',
                                                'aria-required': 'true',
                                                'minlength': '2'}),
            'email': forms.TextInput(attrs={'placeholder': _("Email"),
                                            'name': 'email',
                                            'type': 'email',
                                            'aria-required': 'true',
                                            'minlength': '2'}),
            'phone': forms.TextInput(attrs={'placeholder': _("Phone"),
                                            'name': 'phone',
                                            'type': 'phone',
                                            'aria-required': 'true',
                                            'minlength': '2'}),

        }
