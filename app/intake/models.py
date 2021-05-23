from django.db import models
import requests
import json
import uuid

# from \pdap\master\models.py
from master.models import Dataset



""" 
PDAP Data Intake Schema
These tables are what houses the data ingested from the agencies

When this file is changed: run `python makemigrations` then `python migrate`

If new classes (tables) are added, be sure to add them to the `admin.py` file so they show under /admin
"""

class Incident_Report(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    ccn = models.CharField(max_length=255)
    incidentDate = models.DateTimeField()
    updateDate = models.DateTimeField()
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=2)
    postalCode = models.CharField(max_length=10)
    blocksizedAddress = models.CharField(max_length=255)
    incidentType = models.CharField(max_length=255)
    parentIncidentType = models.CharField(max_length=255)
    narrative = models.CharField(max_length=255)
    dataset = models.ForeignKey(Dataset, null=True, on_delete=models.SET_NULL) 

    class Meta:
        verbose_name_plural = "Incident Reports"

""" Daily Activity Logs / Daily Bulletins """
class Bulletin(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    ReferenceNum = models.CharField(max_length=255)
    ActivityDate = models.DateField()
    ActivityTime = models.TimeField()
    ActivityType = models.CharField(max_length=255)
    ActivityInitator = models.CharField(max_length=255)
    ActivityDescription = models.CharField(max_length=255)
    Disposition = models.CharField(max_length=255)
    ActivityPlace = models.CharField(max_length=255)
    ActivityStreet = models.CharField(max_length=255)
    ActivityCity = models.CharField(max_length=100)
    dataset = models.ForeignKey(Dataset, null=True, on_delete=models.SET_NULL) 
    
    class Meta:
        verbose_name_plural = "Daily Bulletins"

"""
Used in the Proof of Concept, REST API request to DoltHub API
# select * statement from a specified table using the DoltHub API
def get_doltdata(table):
    r = requests.get("https://www.dolthub.com/api/v1alpha1/pdap/datasets/master?q=SELECT%20*%20FROM%20`"+table+"`")
    return r.json()['rows']

def get_agencies_in_state(state):
    r = requests.request("GET", "https://www.dolthub.com/api/v1alpha1/pdap/datasets/master?q=SELECT%20*%20FROM%20`agencies`%20where%20state_iso%20%3D%20'"+state+"'%20order%20by%20name")
    return r.json()['rows']

def get_datasets_for_agency(id):
    r = requests.request("GET", "https://www.dolthub.com/api/v1alpha1/pdap/datasets/master?q=SELECT%20*%20FROM%20`datasets`%20where%20agency_id%20%3D%20'"+id+"'")
    return r.json()['rows']
"""