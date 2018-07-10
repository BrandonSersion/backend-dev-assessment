from django.test import TestCase
from django.core.exceptions import ValidationError as DjangoValidationError
from rest_framework.exceptions import ValidationError as RestValidationError
from unittest import skip
from .factories import CandidateFactory
from ..models import Status


class CandidateModelTest(TestCase):
    def setUp(self):
        self.test_model = CandidateFactory.build()

    def test_name_max_length_valid(self):
        self.test_model.description = 'x' * 256
        self.test_model.full_clean()
        self.test_model.save()

    @skip('Sqlite does not enforce this constraint. Test later with Postgres.')
    def test_name_max_length_invalid(self):
        self.test_model.description = 'x' * 257
        with self.assertRaises(DjangoValidationError):
            self.test_model.full_clean()
            self.test_model.save()

    def test_years_exp_valid(self):
        self.test_model.years_exp = 0
        self.test_model.full_clean()
        self.test_model.save()

        self.test_model.years_exp = 50
        self.test_model.full_clean()
        self.test_model.save()

    def test_years_exp_invalid(self):
        self.test_model.years_exp = 51
        with self.assertRaises(DjangoValidationError):
            self.test_model.full_clean()
            self.test_model.save()

    @skip('Sqlite does not enforce this constraint. Test later with Postgres.')
    def test_years_exp_min_value_invalid(self):
        self.test_model.years_exp = -1
        with self.assertRaises(DjangoValidationError):
            self.test_model.full_clean()
            self.test_model.save()

    def test_status_choices_valid(self):
        self.test_model.status = Status.ACCEPTED
        self.test_model.full_clean()
        self.test_model.save()

        self.test_model.status = Status.PENDING
        self.test_model.full_clean()
        self.test_model.save()

        self.test_model.status = Status.REJECTED
        self.test_model.full_clean()
        self.test_model.save()

    def test_status_choices_invalid(self):
        self.test_model.status = -1
        with self.assertRaises(DjangoValidationError):
            self.test_model.full_clean()
            self.test_model.save()

        self.test_model.status = 4
        with self.assertRaises(DjangoValidationError):
            self.test_model.full_clean()
            self.test_model.save()


class CandidateModelSaveValidationTest(TestCase):
    def setUp(self):
        self.test_model = CandidateFactory.build()
        self.test_model.full_clean()
        self.test_model.save()

    def test_cannot_update_from_accepted_to_rejected(self):
        self.test_model.status = Status.ACCEPTED
        self.test_model.full_clean()
        self.test_model.save()
        with self.assertRaises(RestValidationError):
            self.test_model.status = Status.REJECTED
            self.test_model.full_clean()
            self.test_model.save()

    def test_cannot_update_from_rejected_to_accepted(self):
        self.test_model.status = Status.REJECTED
        self.test_model.full_clean()
        self.test_model.save()
        with self.assertRaises(RestValidationError):
            self.test_model.status = Status.ACCEPTED
            self.test_model.full_clean()
            self.test_model.save()

    def test_reviewed_auto_updates_when_accepted(self):
        self.test_model.status = Status.ACCEPTED
        self.test_model.full_clean()
        self.test_model.save()
        assert self.test_model.reviewed is True

    def test_reviewed_auto_updates_when_rejected(self):
        self.test_model.status = Status.REJECTED
        self.test_model.full_clean()
        self.test_model.save()
        assert self.test_model.reviewed is True

    def test_reviewed_does_not_auto_update_when_left_pending(self):
        self.test_model.description = 'Changed'
        self.test_model.full_clean()
        self.test_model.save()
        assert self.test_model.reviewed is False

    def test_reviewed_does_not_auto_update_when_accepted_to_pending(self):
        # arrange
        self.test_model.status = Status.REJECTED
        self.test_model.full_clean()
        self.test_model.save()
        self.test_model.reviewed = False
        self.test_model.full_clean()
        self.test_model.save()
        # act
        self.test_model.status = Status.PENDING
        self.test_model.full_clean()
        self.test_model.save()
        # assert
        assert self.test_model.reviewed is False

    def test_reviewed_does_not_auto_update_when_rejected_to_pending(self):
        # arrange
        self.test_model.status = Status.ACCEPTED
        self.test_model.full_clean()
        self.test_model.save()
        self.test_model.reviewed = False
        self.test_model.full_clean()
        self.test_model.save()
        # act
        self.test_model.status = Status.PENDING
        self.test_model.full_clean()
        self.test_model.save()
        # assert
        assert self.test_model.reviewed is False