from django.contrib import admin

# Register your models here.
from master.models import Agency_Type, State, County, Agency, Source_Type, Data_Type, Format_Type, Update_Frequency, Scraper, Dataset

admin.site.register(Agency_Type)
admin.site.register(State)
admin.site.register(County)
admin.site.register(Agency)
admin.site.register(Source_Type)
admin.site.register(Data_Type)
admin.site.register(Format_Type)
admin.site.register(Update_Frequency)
admin.site.register(Scraper)
admin.site.register(Dataset)