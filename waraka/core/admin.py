from django.contrib import admin

# Register your models here.
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'owner', 'completed', 'priority')
    search_fields = ('title', 'owner__username')
    list_filter = ('completed', 'priority')

admin.site.register(Task, TaskAdmin)
