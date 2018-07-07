from django.urls import reverse
from django.forms.models import model_to_dict
from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from .factories import CandidateFactory
from ..views import CandidateCRUDView



class TestCandidateCRUDView(APITestCase):    

    def setUp(self):
        self.data = model_to_dict(CandidateFactory.build())
        self.client = APIClient()

    def test_post_valid_candidate(self):
        url = reverse('candidate-list')
        response = self.client.post(url, self.data)
        self.assertEqual(201, response.status_code)

    def test_get_valid_candidate(self):
        url = reverse('candidate-list')
        response = self.client.post(url, self.data)
        url = reverse('candidate-detail', args=[self.data['id']])
        print(url)
        response = self.client.get(url)
        print(response)
        self.assertEqual(response.data, self.data)

    # def test_put_valid_candidate(self):
    #     response = self.client.put(self.url_detail, self.user_data)

    # def test_delete_valid_candidate(self):
    #     response = self.client.delete(self.url_detail)
    #     self.assertEqual(204, response.status_code)


class TestCandidateListView(APITestCase):
    def setUp(self):
        # self.url = reverse('')
        self.user_data = model_to_dict(CandidateFactory.build())

