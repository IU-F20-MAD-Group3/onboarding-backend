from rest_framework import viewsets, mixins
from rest_framework.permissions import IsAuthenticated

from .models import Checklist
from .serializers import ChecklistSerializer


class ChecklistViewSet(
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    viewsets.GenericViewSet,
):
    """A viewset for viewing checklist instances.

    Provides `list` and `retrieve` actions.

    """
    queryset = Checklist.objects.all()
    serializer_class = ChecklistSerializer

    permission_classes = [IsAuthenticated]
