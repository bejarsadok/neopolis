from django.contrib import admin
from .models import Project, Task
# Register your models here.


class ProjectAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "name",
        "description",
        "get_members",
    )
    list_filter = (
        "name",
    )
    search_fields = ("id", "name")

    def get_members(self, obj):
        return ", ".join(member.username for member in obj.members.all())
    get_members.short_description = 'Members'

admin.site.register(Project, ProjectAdmin)


class TaskAdmin(admin.ModelAdmin):
    def project_label(self, obj):
        return obj.project.name if obj.project else 'No Project'
    project_label.short_description = "Project"

    list_display = (
        "id",
        "title",
        "description",
        "due_date",
        "completed",
        "project_label",
        "assiged_to",
    )
    list_filter = (
        "title", 
        "due_date",
        "project",
        "assiged_to",
    )
    search_fields = ("id", "title", "due_date")

# Enregistrer le modèle Task avec le modèle d'administration TaskAdmin
admin.site.register(Task, TaskAdmin)
