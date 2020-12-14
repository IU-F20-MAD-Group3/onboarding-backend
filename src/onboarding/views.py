from rest_framework import viewsets, mixins
from rest_framework.permissions import IsAuthenticated

from .models import Checklist
from .serializers import ChecklistSerializer
from .permissions import IsMember


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

    permission_classes = [IsAuthenticated, IsMember]

    def get_queryset(self):
        """Get a queryset of checklists from a user's organization.
        """
        user = self.request.user
        organization = user.member.organization
        return organization.checklists.all()
