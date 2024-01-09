from django.test import Client, RequestFactory

from .base_class import BaseTestClass
from ..models import QuizData, QuizObject
from ..views import index


class TestQuizView(BaseTestClass):

    def setUp(self) -> None:
        self._client = Client()
        # Let's create the required data for the view
        quiz_obj = QuizObject.objects.create(
            quiz_title="Test quiz",
            quiz_category="Test category"
        )
        QuizData.objects.create(
            quiz_obj=quiz_obj,
            quiz_question="quiz question",
            choice_1="choice1",
            choice_2="choice2",
            choice_3="choice3",
            choice_4="choice4",
            response="answer"
        )
    
    def test_index_view(self):
        # Make a Get request and assess the returned response contents
        response = self._client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context.template_name, "quiz.html")
        context_value = {
            "quiz_title" : "Test quiz",
            "quiz_quest" : "quiz question",
            "choices" : ['choice1', 'choice2', 'choice3', 'choice4'],
            "response" : "answer"
        }
        for key, value in context_value.items():
            self.assertEqual(response.context[key], value)


class TestQuizViewWithRequestFactory(BaseTestClass):

    def setUp(self) -> None:
        self.fact = RequestFactory() # Create the RequestFactory instance
        # Let's create the required data for the view
        quiz_obj = QuizObject.objects.create(
            quiz_title="Test quiz",
            quiz_category="Test category"
        )
        QuizData.objects.create(
            quiz_obj=quiz_obj,
            quiz_question="quiz question",
            choice_1="choice1",
            choice_2="choice2",
            choice_3="choice3",
            choice_4="choice4",
            response="answer"
        )
    
    def test_index_view(self):
        # Create a Get request and call the view with that

        get_req = self.fact.get('/') # Create the WSGI object
        response = index(get_req) # Calling the view like a function with the WSGI object
        
        self.assertEqual(response.status_code, 200)
        