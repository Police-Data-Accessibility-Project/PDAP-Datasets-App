from django.contrib import admin

from intake.models import Bulletin, Incident_Report

# Register your models here.
admin.site.register(Bulletin)
admin.site.register(Incident_Report)