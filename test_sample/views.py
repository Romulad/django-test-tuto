from django.shortcuts import render

from .models import QuizData, QuizObject


def index(request):
    first_quiz = QuizObject.objects.all()[0]
    quiz_data = QuizData.objects.filter(quiz_obj=first_quiz)[0]
    choices = ["choice_1", "choice_2", "choice_3", "choice_4"]

    context = {
        "quiz_title" : first_quiz.quiz_title,
        "quiz_quest" : quiz_data.quiz_question,
        "choices" : [getattr(quiz_data, c) for c in choices],
        "response" : quiz_data.response
    }
    return render(request, "quiz.html", context)
