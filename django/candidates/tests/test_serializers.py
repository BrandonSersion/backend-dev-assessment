from django.forms.models import model_to_dict
from rest_framework.test import APITestCase
from .factories import CandidateFactory
from ..serializers import CandidateCRUDSerializer


class TestCandidateCRUDSerializer(APITestCase):
    def setUp(self):
        self.user_data = model_to_dict(CandidateFactory.build())

    def test_serializer_with_empty_data(self):
        serializer = CandidateCRUDSerializer(data={})
        assert not serializer.is_valid()

    def test_serializer_with_valid_data(self):
        serializer = CandidateCRUDSerializer(data=self.user_data)
        assert serializer.is_valid()


class TestCandidateListSerializer(APITestCase):
    def setUp(self):
        self.user_data = model_to_dict(CandidateFactory.build())