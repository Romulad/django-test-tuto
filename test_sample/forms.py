from django import forms
from django.utils.translation import gettext_lazy as _


class ContactForm(forms.Form):
    name = forms.CharField(
        required=True,
        label=_('Name'),
        widget=forms.TextInput(
            attrs={
                "placeholder" : _("your name"),
                "class" : "form-control mb-3 border-radius py-3"
            }
        )
    )

    email = forms.CharField(
        required=True,
        label=_('Email'),
        widget=forms.EmailInput(
            attrs={
                "placeholder" : _("valid email"),
                "class" : "form-control mb-3 border-radius py-3"
            }
        )
    )

    message = forms.CharField(
        required=True,
        label=_('Tell us'),
        widget=forms.Textarea(
            attrs={
                "placeholder" : _("your message"), 'cols': '30', 'rows': '10',
                "class" : "form-control mb-3 border-radius"
            }
        )
    )

    def clean_message(self):
        message = self.cleaned_data["message"]
        if len(message) < 3:
            raise forms.ValidationError(_('Your message is too short'))
        return message