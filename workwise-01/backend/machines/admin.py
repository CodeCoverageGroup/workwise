from django.contrib import admin
from .models import Machine
from .models import MaintenanceTicket

@admin.register(MaintenanceTicket)
class MaintenanceTicketAdmin(admin.ModelAdmin):
    list_display = ('machine', 'issue_description', 'reported_by', 'status', 'created_at', 'updated_at')
    search_fields = ('machine__name', 'issue_description', 'status')
    list_filter = ('status', 'created_at', 'updated_at')

@admin.register(Machine)
class MachineAdmin(admin.ModelAdmin):
    list_display = ('name', 'model_number', 'status', 'location', 'last_maintenance_date')
    search_fields = ('name', 'model_number', 'status', 'location')
    list_filter = ('status', 'location', 'last_maintenance_date')
