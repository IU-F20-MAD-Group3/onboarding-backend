from django.contrib import admin

from . import models

admin.site.register(models.Organization)
admin.site.register(models.Member)
admin.site.register(models.Checklist)
admin.site.register(models.ChecklistParticipation)
admin.site.register(models.Task)
admin.site.register(models.TaskExecution)
admin.site.register(models.News)
