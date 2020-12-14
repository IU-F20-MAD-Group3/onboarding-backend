from rest_framework import serializers

from .models import Checklist, Task, TaskExecution


class ChecklistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Checklist
        fields = ('id', 'name', 'description')
        read_only_fields = fields


class TaskSerializer(serializers.ModelSerializer):
    status = serializers.SerializerMethodField('task_status')

    def task_status(self, task):
        user = self.context['request'].user
        member = user.member

        try:
            task_exec = TaskExecution.objects.get(member=member, task=task)
            status = task_exec.get_status_display()
        except TaskExecution.DoesNotExist:
            status = TaskExecution.STATUS_PENDING_DISPLAY

        return status

    class Meta:
        model = Task
        fields = ('id', 'name', 'description', 'status')
        read_only_fields = fields
