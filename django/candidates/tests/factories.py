from factory.django import DjangoModelFactory
from factory import Faker, Sequence
from random import randint, choice
from ..models import Status


class CandidateFactory(DjangoModelFactory):

    class Meta:
        model = 'candidates.Candidate'

    id = 2
    name = Faker('name')
    years_exp = randint(0, 50)
    status = choice([Status.PENDING, Status.ACCEPTED, Status.REJECTED])
    date_applied = Faker('date_time')
    reviewed = Faker('boolean')
    description = Faker('sentence')

    created = Faker('date_time')
    updated = Faker('date_time')
