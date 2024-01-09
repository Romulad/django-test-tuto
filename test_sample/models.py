from django.db import models
from django.utils.translation import gettext_lazy as _


class QuizObject(models.Model):
    """Represents a quiz"""
    quiz_title = models.CharField(_('Quiz Title'), max_length=200, default="", unique=True)
    quiz_category = models.CharField(_('Quiz Category'), max_length=200, default="")

    class Meta:
        verbose_name = _('Quiz Object')
        verbose_name_plural = _('Quiz Objects')

    def __str__(self) -> str:
        return self.quiz_title
    
    @classmethod
    def filter_by_cate(cls, category):
        """Returns all the quiz objects with the given category"""
        return cls.objects.filter(quiz_category=category)


class QuizData(models.Model):
    """Stores questions and choices about a quiz"""
    quiz_obj = models.ForeignKey(
        QuizObject, on_delete=models.CASCADE, verbose_name=_('Quiz about')
    )
    quiz_question = models.CharField(_('Quiz question'), max_length=1000, default="")
    choice_1 = models.CharField(_('Choice one'), max_length=1000, default="")
    choice_2 = models.CharField(_('Choice two'), max_length=1000, default="")
    choice_3 = models.CharField(_('Choice three'), max_length=1000, default="")
    choice_4 = models.CharField(_('Choice four'), max_length=1000, default="")
    response = models.CharField(_('Answer'), max_length=1000, default="")

    class Meta:
        verbose_name = _('Quiz data')
        verbose_name_plural = _('Quiz datas')

    def __str__(self) -> str:
        return self.quiz_obj.quiz_title
