from django.utils.translation import gettext_lazy as _
from django.db import models

from ..models import QuizObject, QuizData
from .base_class import BaseTestClass # Subclass of TestCase provided by Django


class TestQuizModel(BaseTestClass):
    model_object = QuizObject
    
    def test_model_fields(self):
         
        # Field : quiz_title
        self.assertEqual(
            self.model_object.quiz_title.field.verbose_name, _('Quiz Title')
        ) # check field verbose_name
        self.assertEqual(
            self.model_object.quiz_title.field.default, ""
        ) # check field default value
        self.assertEqual(
            self.model_object.quiz_title.field.max_length, 200
        ) # check field max_length
        self.assertEqual(
            self.model_object.quiz_title.field.unique, True
        ) # check field unique value

        # quiz_category
        self.assert_object_attr(
            self.model_object.quiz_category.field,
            verbose_name = _('Quiz Category'), 
            default = "", 
            max_length = 200
        )

    def test_model_meta_data(self):
        self.assert_object_attr(
            self.model_object._meta,
            verbose_name = _('Quiz Object'), 
            verbose_name_plural = _('Quiz Objects') 
        )
        
    def test_filter_by_cate(self):
        """Test if `QuizObject.filter_by_cate` returns datas filtered by category"""

        datas = [
            ("Les chats", "Animaux"), 
            ("Marathon", "Sport"),
            ("Les chiens", "Animaux"), 
            ("Foot", "Sport"),
        ]
        for data in datas:
            self.model_object.objects.create(
                quiz_title = data[0],
                quiz_category = data[1]
            )

        resul = self.model_object.filter_by_cate(datas[0][1])
        self.assertEqual(len(resul), 2)
        self.assertEqual(resul[0].quiz_title, datas[0][0])
        self.assertEqual(resul[1].quiz_title, datas[2][0])

        # __str__
        self.assertEqual(resul[0].__str__(), resul[0].quiz_title)


class TestQuizDataModel(BaseTestClass):
    model_object = QuizData

    def test_model_fields(self):

        # quiz_obj
        self.assert_object_attr(
            self.model_object.quiz_obj.field.remote_field,
            model=QuizObject,
            on_delete=models.CASCADE,
        ) # For the foreign relationship with QuizObject
        self.assert_object_attr(
            self.model_object.quiz_obj.field,
            verbose_name=_('Quiz about')
        )  # For the contents of model_object

        # The other fields
        # Each tuple in the list below contain : a field name,
        # a dict that has as key the attribut name to test
        # and as value the except attr value
        other_fields = [
            ("quiz_question", {"verbose_name" : _('Quiz question')}),
            ("choice_1", {"verbose_name" : _('Choice one')}),
            ("choice_2", {"verbose_name" : _('Choice two')}),
            ("choice_3", {"verbose_name" : _('Choice three')}),
            ("choice_4", {"verbose_name" : _('Choice four')}),
            ("response", {"verbose_name" : _('Answer')})
        ]
        for field in other_fields:
            self.assert_object_attr(
                getattr(getattr(self.model_object, field[0]), 'field'),
                **field[1],
                max_length=1000, # This is a common arg for the fields
                default="" # This is a common arg for the fields 
            )
    
    def test_model_meta_data(self):
        self.assert_object_attr(
            self.model_object._meta,
            verbose_name = _('Quiz data'), 
            verbose_name_plural = _('Quiz datas')
        )

        
