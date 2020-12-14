from rest_framework import viewsets, mixins
from rest_framework.permissions import IsAuthenticated

from .models import Checklist, Task
from .serializers import ChecklistSerializer, TaskSerializer
from .permissions import IsMember


class ChecklistViewSet(
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    viewsets.GenericViewSet,
):
    """A viewset for viewing checklist instances.

    Provides `list` and `retrieve` actions.

    """
    serializer_class = ChecklistSerializer
    permission_classes = [IsAuthenticated, IsMember]

    def get_queryset(self):
        """Get a queryset of checklists from a user's organization.
        """
        user = self.request.user
        organization = user.member.organization
        return organization.checklists.all()


class TaskViewSet(
    mixins.RetrieveModelMixin,
    viewsets.GenericViewSet,
):
    """A viewset for retrieving task instances.

    Provides `retrieve` action.

    """
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated, IsMember]

    def get_queryset(self):
        """Get a queryset of tasks from a user's organization.
        """
        user = self.request.user
        organization = user.member.organization
        return Task.objects.filter(checklist__organization=organization)
