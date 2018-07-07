from rest_framework import serializers
from .models import Candidate
from .validators import RestrictStatusUpdate


class CandidateSerializer(serializers.ModelSerializer):
    """
    Serializes Candidate.
    """
    class Meta:
        model = Candidate
        fields = (
            'id',
            'name',
            'years_exp',
            'status',
            'date_applied',
            'reviewed',
            'description',
            'created',
            'updated',
        )



    #     validators = [RestrictStatusUpdate('status')]

    # def validate_status(self, value):
    #     self.status = value
    #     print(value)
    #     return value