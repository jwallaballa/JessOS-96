from django.contrib import admin
from .models import Project, ActiveThought

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'role', 'timeline', 'impact_metric', 'order')
    list_editable = ('order',)
    search_fields = ('title', 'description', 'subtitle')

@admin.register(ActiveThought)
class ActiveThoughtAdmin(admin.ModelAdmin):
    list_display = ('phrase', 'created_at')
    ordering = ('-created_at',)