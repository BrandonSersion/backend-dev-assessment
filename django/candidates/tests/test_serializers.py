from django.test import TestCase
from django.forms.models import model_to_dict
from .factories import CandidateFactory


class TestCandidateCRUDSerializer(TestCase):
    def setUp(self):
        self.user_data = model_to_dict(CandidateFactory.build())


class TestCandidateListSerializer(TestCase):
    def setUp(self):
        self.user_data = model_to_dict(CandidateFactory.build())