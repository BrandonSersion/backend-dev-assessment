from rest_framework import serializers
from .models import Candidate


class CandidateCRUDSerializer(serializers.ModelSerializer):
    """
    Serializes Candidate create, read, update, delete.
    """
    class Meta:
        model = Candidate
        fields = (
            'name',
            'years_exp',
            'status',
            'date_applied',
            'reviewed',
            'description',
            'created',
            'updated',
        )
        
