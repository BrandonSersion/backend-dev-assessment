from random import randint
from factory.django import DjangoModelFactory
from factory import Faker
from ..models import Status


class CandidateFactory(DjangoModelFactory):
    class Meta:
        model = 'candidates.Candidate'

    id = randint(10000, 1000000)
    name = Faker('name')
    years_exp = randint(0, 50)
    status = Status.PENDING
    date_applied = Faker('date_time')
    reviewed = False
    description = Faker('sentence')
    created = Faker('date_time')
    updated = Faker('date_time')
