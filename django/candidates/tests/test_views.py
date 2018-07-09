from django.core.urlresolvers import reverse
from django.forms.models import model_to_dict
from rest_framework.test import APITestCase
from .factories import CandidateFactory


class TestCandidateViews(APITestCase):
    def setUp(self):
        self.data = model_to_dict(CandidateFactory.build())
        # Override id with one that exists in production to test retrieve, update, delete.
        # TODO replace with fixture or other solution.
        self.data['id'] = 2
        self.candidate_list_url = reverse('candidate-list')
        self.candidate_detail_url = reverse('candidate-detail', args=[self.data['id']])
        self.candidates_list_url = reverse('candidates-list')

    def test_create_candidate(self):
        response = self.client.post(self.candidate_list_url, self.data)
        self.assertEqual(201, response.status_code)

    def test_retrieve_candidate(self):
        response = self.client.get(self.candidate_detail_url)
        self.assertEqual(200, response.status_code)

    def test_update_candidate(self):
        response = self.client.patch(self.candidate_detail_url, {'description': 'New description.'})
        self.assertEqual(200, response.status_code)

    def test_delete_candidate(self):
        response = self.client.delete(self.candidate_detail_url)
        self.assertEqual(204, response.status_code)

    def test_list_candidate(self):
        response = self.client.get(self.candidates_list_url)
        self.assertEqual(200, response.status_code)
