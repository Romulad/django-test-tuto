from django.apps import AppConfig


class TestSampleConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'test_sample'
    verbose_name = "Quiz"
