from django.forms.models import model_to_dict
from rest_framework.test import APITestCase
from .factories import CandidateFactory


class TestCandidateCRUDView(APITestCase):
    def setUp(self):
        # self.url = reverse('')
        self.user_data = model_to_dict(CandidateFactory.build())


class TestCandidateListView(APITestCase):
    def setUp(self):
        # self.url = reverse('')
        self.user_data = model_to_dict(CandidateFactory.build())

