from rest_framework import serializers
from .models import Candidate


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
        
