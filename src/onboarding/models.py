from django.db import models
from django.contrib.auth.models import User


class Organization(models.Model):
    name = models.CharField(max_length=256)

    def __str__(self):
        return self.name


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

    def __str__(self):
        return str(self.user)


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

    def __str__(self):
        return self.name


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

    def __str__(self):
        return f"{self.member} in {self.checklist}"


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

    def __str__(self):
        return self.name


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

    def __str__(self):
        return f"{self.member} in {self.task}"


class News(models.Model):
    title = models.CharField(max_length=128)
    text = models.TextField()

    organization = models.ForeignKey(
        Organization,
        on_delete=models.CASCADE,
        related_name='news',
    )

    def __str__(self):
        return self.title
