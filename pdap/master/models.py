from django.db import models
import uuid

""" 
PDAP Master Schema
These tables are mainly the reference tables, agencies and datasets

When this file is changed: run `python makemigrations` then `python migrate`

If new classes (tables) are added, be sure to add them to the `admin.py` file so they show under /admin
"""

""" the type of agency [federal / state / county / municipal .etc] """
class Agency_Type(models.Model):
    # technically, this would automatically be created without specifying
    # but for anyone not familiar with Django, I am manually putting it here
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = "Agency Types"

""" list of US States like {'name_iso': 'CA', 'name': 'California'} """
class State(models.Model):
    name_iso = models.CharField(max_length=2, primary_key=True)
    name = models.CharField(max_length=50)

    
""" list of US Counties with official 5 digit county FIPS code """
class County(models.Model):
    fips = models.CharField(max_length=5, primary_key=True)
    name = models.CharField(max_length=100)
    name_ascii = models.CharField(max_length=100)
    state_iso = models.ForeignKey(State, null=True, on_delete=models.SET_NULL)
    lat = models.FloatField()
    lng = models.FloatField()
    population = models.IntegerField(null=True)

    class Meta:
        verbose_name_plural = "Counties"

""" agency master table """
class Agency(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=150)
    agency_type = models.ForeignKey(Agency_Type, null=True, on_delete=models.SET_NULL) # if the agency_type is deleted, set it null
    state_iso = models.ForeignKey(State, null=True, on_delete=models.SET_NULL)
    city = models.CharField(max_length=150, null=True)
    zipcode = models.IntegerField(null=True)
    county_fips = models.ForeignKey(County, null=True, on_delete=models.SET_NULL)
    lat = models.FloatField(null=True)
    lng = models.FloatField(null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    data_policy = models.CharField(max_length=1000, null=True)
    country = models.CharField(max_length=2, default='US', null=True)
    homepage_url = models.CharField(max_length=1000, null=True)

    class Meta:
        verbose_name_plural = "Agencies"

""" source types [court / direct / third party .etc] """
class Source_Type(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=50)
    description = models.TextField(null=True)

    class Meta:
        verbose_name_plural = "Source Types"

""" data types [incident_report / daily_bulletin / bodycam_footage .etc] """
class Data_Type(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=50)
    description = models.TextField(null=True)

    class Meta:
        verbose_name_plural = "Data Types"

""" format types [nibrs / cityprotect / opendata .etc] """
class Format_Type(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=50)
    description = models.TextField(null=True)

    class Meta:
        verbose_name_plural = "Format Types"

""" update frequency [yearly / monthly / quarterly .etc] """
class Update_Frequency(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=50)
    description = models.TextField(null=True)
    class Meta:
        verbose_name_plural = "Update Frequencies"

""" information on scrapers """
class Scraper(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False) 
    path = models.CharField(max_length=50)
    description = models.TextField(null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

""" Current Status of Datasets (added 14 May 2021) """
class Dataset_Status(models.Model):
    id = models.BigAutoField(primary_key=True)
    description = models.CharField(max_length=255)


""" datasets master table """
class Dataset(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    url = models.CharField(max_length=255, unique=True)
    status = models.ForeignKey(Dataset_Status, null=True, on_delete=models.SET_NULL)
    source_type = models.ForeignKey(Source_Type, null=True, on_delete=models.SET_NULL)
    data_type = models.ForeignKey(Data_Type, null=True, on_delete=models.SET_NULL)
    format_type = models.ForeignKey(Format_Type, null=True, on_delete=models.SET_NULL)
    agency = models.ForeignKey(Agency, null=True, on_delete=models.SET_NULL)
    update_frequency = models.ForeignKey(Update_Frequency, null=True, on_delete=models.SET_NULL)
    portal_type = models.CharField(max_length=255, null=True)
    coverage_start = models.DateField(null=True)
    scraper = models.ForeignKey(Scraper, null=True, on_delete=models.SET_NULL)
    can_scrape = models.BooleanField(default=1, null=True)
    notes = models.TextField(null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    machine_readable = models.BooleanField(null=True)

