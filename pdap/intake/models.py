from django.db import models
import requests
import json

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