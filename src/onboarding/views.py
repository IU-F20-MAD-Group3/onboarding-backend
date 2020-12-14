from http import HTTPStatus

from rest_framework import viewsets, mixins
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import Task, TaskExecution
from .serializers import ChecklistSerializer, TaskSerializer
from .permissions import IsMember


class ChecklistViewSet(
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    viewsets.GenericViewSet,
):
    """A viewset for viewing checklist instances.

    Provides `list`, `retrieve` and `tasks` actions.

    """
    serializer_class = ChecklistSerializer
    permission_classes = [IsAuthenticated, IsMember]

    def get_queryset(self):
        """Get a queryset of checklists from a user's organization.
        """
        user = self.request.user
        organization = user.member.organization
        return organization.checklists.all()

    @action(detail=True, methods=['get'], serializer_class=TaskSerializer)
    def tasks(self, request, pk=None):
        checklist = self.get_object()
        tasks = checklist.tasks.all()
        serializer = self.get_serializer(tasks, many=True)
        return Response(serializer.data)


class TaskViewSet(
    mixins.RetrieveModelMixin,
    viewsets.GenericViewSet,
):
    """A viewset for retrieving task instances.

    Provides `retrieve` and `finish` actions.

    """
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated, IsMember]

    def get_queryset(self):
        """Get a queryset of tasks from a user's organization.
        """
        user = self.request.user
        organization = user.member.organization
        return Task.objects.filter(checklist__organization=organization)

    @action(detail=True, methods=['post'])
    def finish(self, request, pk=None):
        """Updates task's status to finished.
        """
        user = self.request.user
        member = user.member
        task = self.get_object()

        TaskExecution.objects.update_or_create(
            member=member,
            task=task,
            defaults={'status': TaskExecution.STATUS_FINISHED},
        )

        return Response(status=HTTPStatus.NO_CONTENT)
