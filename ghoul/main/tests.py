from django.test import TestCase
from .forms import *   # import all forms
from django.core.files.uploadedfile import SimpleUploadedFile


class Articles_Form_Test(TestCase):

    def test_basic_addition(self):
        form = CityForm({'name': 'test', 'placeholder': "test"})
        self.assertTrue(form.is_valid())

    def test_ArticlesForm_invalid(self):
        form = CityForm({'name': "", 'placeholder': ""})
        self.assertFalse(form.is_valid())

