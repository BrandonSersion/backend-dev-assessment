from factory.django import DjangoModelFactory
from factory import Faker, Sequence
from random import randint, choice
from ..models import Candidate


class CandidateFactory(DjangoModelFactory):

    class Meta:
        model = 'candidates.Candidate'

    id = 2
    name = Faker('name')
    years_exp = randint(0, 99)
    status = choice([Candidate.PENDING, Candidate.ACCEPTED, Candidate.REJECTED])
    date_applied = Faker('date_time')
    reviewed = Faker('boolean')
    description = Faker('sentence')

    created = Faker('date_time')
    updated = Faker('date_time')
