from django import forms
from django.utils.translation import gettext_lazy as _

from .base_class import BaseTestClass
from ..forms import ContactForm


class TestContactForm(BaseTestClass):
    form_obj = ContactForm
    field_count = 3
    
    def test_message_validation(self):
        # Must raise an exception
        self.form_obj.cleaned_data = {"message": "Hi"}
        with self.assertRaises(forms.ValidationError) as err_obj:
            self.form_obj().clean_message()
        self.assertEqual(err_obj.exception.message, _('Your message is too short'))
        
        # Correct
        right_mess = "Hello, How to add a new quiz to the website?"
        self.form_obj.cleaned_data = {"message": right_mess}
        self.assertEqual(self.form_obj().clean_message(), right_mess)
    
    def test_form_content(self):
        self.global_form_test()

        # name, email, message
        all_fields = [
            {
                "cur_field":"name",
                "field_class" : forms.CharField,
                "required" : True,
                "label" : _('Name'),
                "widget" : forms.TextInput,
                "widget_attrs" :  { 
                    "placeholder" : _("your name"), 
                    "class" : "form-control mb-3 border-radius py-3"}
            },
            {
                "cur_field":"email",
                "field_class" : forms.CharField,
                "required" : True,
                "label" : _('Email'),
                "widget" : forms.EmailInput,
                "widget_attrs" :  { 
                    "placeholder" : _("valid email"),
                    "class" : "form-control mb-3 border-radius py-3"}
            },
            {
                "cur_field":"message", 
                "field_class" : forms.CharField,
                "required" : True,
                "label" : _('Tell us'),
                "widget" : forms.Textarea,
                "widget_attrs" :  {
                "placeholder" : _("your message"), 'cols': '30', 'rows': '10',
                "class" : "form-control mb-3 border-radius"}
            },
        ]
        
        for field in all_fields:
            self.assert_form_content(
                **field
            )
