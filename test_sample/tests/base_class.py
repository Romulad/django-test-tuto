from inspect import isclass, isfunction

from django.test import TestCase
from django import forms


class BaseTestClass(TestCase):
    
    def assert_object_attr(self, obj, **kwargs):
        """Assert an obj with the list of it attributes"""
        for attr, value in kwargs.items():
            if isclass(value) or isfunction(value):
                self.assertIs(getattr(obj, attr), value)
            else:
                self.assertEqual(getattr(obj, attr), value)
    
    def global_form_test(self):
        self.assertEqual(len(self.form_obj.base_fields), self.field_count)
        self.assertIsInstance(self.form_obj(), forms.Form)
    
    def assert_form_content(self, **kwargs):
        """Tests the contents of the form"""
        obj = self.form_obj.base_fields[kwargs.pop("cur_field")]

        self.assertIsInstance(
            obj, kwargs.pop("field_class")
        ) # Field instance class
        self.assertEqual(
            getattr(obj.widget, "attrs"), kwargs.pop("widget_attrs")
        ) # widget attrs
        for attr, value in kwargs.items():
            if isclass(value):
                self.assertIsInstance(getattr(obj, attr), value)
            else:
                self.assertEqual(getattr(obj, attr), value)