from django.core.urlresolvers import reverse, resolve
from django.forms.models import model_to_dict
from rest_framework import test
from .factories import CandidateFactory


class TestCandidateViews(test.APITestCase):   
    def setUp(self):
        self.data = model_to_dict(CandidateFactory.build())
        self.client = test.APIClient()

    def test_create_candidate(self):
        url = reverse('candidate-list')
        response = self.client.post(url, self.data)
        self.assertEqual(201, response.status_code)

    def test_retreive_candidate(self):
        url = reverse('candidate-detail', args=[self.data['id']])
        response = self.client.get(url)
        self.assertEqual(200, response.status_code)

    def test_update_candidate(self):
        url = reverse('candidate-detail', args=[self.data['id']])
        response = self.client.patch(url, {'description': 'New description.'})
        self.assertEqual(200, response.status_code)

    def test_delete_candidate(self):
        url = reverse('candidate-detail', args=[self.data['id']])
        response = self.client.delete(url)
        self.assertEqual(204, response.status_code)

    def test_list_candidate(self):
        url = reverse('candidates-list')
        response = self.client.get(url)
        self.assertEqual(200, response.status_code)
