from django.contrib import admin
from task import models


@admin.register(models.Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = 'id', 'name_task', 'created_date','owner'
    ordering = '-id',


@admin.register(models.Setor)
class SetorAdmin(admin.ModelAdmin):
    list_display = 'id', 'name'
    ordering = '-id',