from django import forms
from dashboard.models import Members, SoberBros
from django.core import validators
from django.utils.translation import ugettext_lazy as _
from django.forms import ValidationError
# from bootstrap_modal_forms.forms import BSModalForm

# def check_for_z(value):
#     if value[0].lower() != 'z':
#         raise forms.ValidationError("NAME NEEDS TO START WITH Z")

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Members
        fields = ['name', 'legal_name', 'phone', 'address', 'email', 'avatar']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control',
                                           'type': 'text',
                                           'name': 'Name',
                                           'id': 'full_name',
                                           'title': 'Your current name.',
                                           'value': '{{ me.name }}'}),
            'legal_name': forms.TextInput(attrs={'class': 'form-control',
                                                 'type': 'text',
                                                 'name': 'Legal Name',
                                                 'id': 'legal_name',
                                                 'title': 'Your current legal name.',
                                                 'value': '{{ me.legal_name }}'}),
            'phone': forms.TextInput(attrs={'class': 'form-control',
                                            'type': 'text',
                                            'name': 'Phone Number',
                                            'id': 'phone',
                                            'title': 'Your current phone number.',
                                            'value': '{{ me.phone }}'}),
            'email': forms.EmailInput(attrs={'class': 'form-control',
                                             'type': 'email',
                                             'name': 'Email Address',
                                             'id': 'email',
                                             'title': 'Your current email.',
                                             'value': '{{ me.email }}'}),
            'address': forms.TextInput(attrs={'class': 'form-control',
                                              'type': 'text',
                                              'name': 'Address',
                                              'id': 'address',
                                              'title': 'Your current address.',
                                              'value': '{{ me.address }}'}),
            'avatar': forms.FileInput(attrs={
                'name': "avatar",
                'type': "file",
                'accept': 'image/*',
            })
        }
        labels = {
            "name": _("Name"),
            "legal_name": _("Legal Name"),
            "phone": _("Phone"),
            "email": _("Email"),
            "address": _("Address"),
        }

    def clean_name(self):
        processed = self.cleaned_data['name'].split(" ")
        result = ""

        if len(processed) == 1:
            raise ValidationError("I'm sorry, it would appear you only have entered your first name.")

        for x in range(len(processed)):
            result = result + processed[x].capitalize() + " "

        return result.strip()

    def clean(self):
        all_clean_data = super().clean()
        print("CLEANED: " + str(all_clean_data))


class SoberBroSignupForm(forms.ModelForm):
    class Meta:
        model = SoberBros
        exclude = ['id']

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super(SoberBroSignupForm, self).__init__(*args, **kwargs)
