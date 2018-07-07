from django_filters import rest_framework as df_filters
from rest_framework import mixins, viewsets, filters
from .models import Candidate
from .serializers import CandidateSerializer


class CandidateCRUDView(mixins.CreateModelMixin,
                        mixins.RetrieveModelMixin,
                        mixins.UpdateModelMixin,
                        mixins.DestroyModelMixin,
                        viewsets.GenericViewSet):
    queryset = Candidate.objects.all()
    serializer_class = CandidateSerializer


class CandidateListView(mixins.ListModelMixin,
                        viewsets.GenericViewSet):
    queryset = Candidate.objects.all()
    serializer_class = CandidateSerializer
    filter_backends = (df_filters.DjangoFilterBackend, filters.OrderingFilter,)
    filter_fields = ('reviewed',)
    ordering_fields = ('status', 'date_applied',)