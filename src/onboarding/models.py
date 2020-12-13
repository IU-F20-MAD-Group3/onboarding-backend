from django.db import models
from django.contrib.auth.models import User


class Organization(models.Model):
    name = models.CharField(max_length=256)


class Member(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name='member',
    )

    organization = models.ForeignKey(
        Organization,
        on_delete=models.CASCADE,
        related_name='members',
    )


class Checklist(models.Model):
    name = models.CharField(max_length=128)
    description = models.TextField()

    organization = models.ForeignKey(
        Organization,
        on_delete=models.CASCADE,
        related_name='checklists',
    )

    members = models.ManyToManyField(
        Member,
        through='ChecklistParticipation',
        related_name='checklists',
    )


class ChecklistParticipation(models.Model):
    checklist = models.ForeignKey(
        Checklist,
        on_delete=models.CASCADE,
        related_name='participations',
    )

    member = models.ForeignKey(
        Member,
        on_delete=models.CASCADE,
        related_name='checklist_participations',
    )


class Task(models.Model):
    name = models.CharField(max_length=128)
    description = models.TextField()

    checklist = models.ForeignKey(
        Checklist,
        on_delete=models.CASCADE,
        related_name='tasks',
    )

    members = models.ManyToManyField(
        Member,
        through='TaskExecution',
        related_name='tasks',
    )


class TaskExecution(models.Model):
    task = models.ForeignKey(
        Task,
        on_delete=models.CASCADE,
        related_name='executions',
    )

    member = models.ForeignKey(
        Member,
        on_delete=models.CASCADE,
        related_name='task_executions',
    )

    STATUS_PENDING = 'pndg'
    STATUS_FINISHED = 'fnsh'

    STATUS_CHOICES = (
        (STATUS_PENDING, 'Pending'),
        (STATUS_FINISHED, 'Finished'),
    )

    status = models.CharField(
        max_length=4,
        choices=STATUS_CHOICES,
        default=STATUS_PENDING,
    )


class News(models.Model):
    title = models.CharField(max_length=128)
    text = models.TextField()

    organization = models.ForeignKey(
        Organization,
        on_delete=models.CASCADE,
        related_name='news',
    )
