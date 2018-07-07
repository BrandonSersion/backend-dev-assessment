from rest_framework import mixins, viewsets
from .models import Candidate
from .serializers import CandidateSerializer


class CandidateCRUDView(mixins.CreateModelMixin,
                        mixins.RetrieveModelMixin,
                        mixins.UpdateModelMixin,
                        mixins.DestroyModelMixin,
                        viewsets.GenericViewSet):
    queryset = Candidate.objects.all()
    serializer_class = CandidateSerializer
    lookup_field = "id"

# class CandidateListView(mixins.ListModelMixin,
#                         viewsets.GenericViewSet):
#     queryset = Candidate.objects.all()
#     serializer_class = CandidateCRUDSerializer
