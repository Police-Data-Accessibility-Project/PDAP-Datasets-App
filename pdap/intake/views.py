from django.shortcuts import render
from .models import get_doltdata, get_agencies_in_state, get_datasets_for_agency
from django.http import JsonResponse

# Create your views here.
def index(request):
    states = get_doltdata('states')
    data_types = get_doltdata('data_types')
    format_types = get_doltdata('format_types')
    source_types = get_doltdata('source_types')
    update = get_doltdata('update_frequency')
    context = {'states': states, 'data_types': data_types, 'format_types': format_types, 'source_types': source_types, 'update': update}
    return render(request, 'index.html', context=context)

# similar to above but built specifically for scrapers to auto-build the schema.json
def schema(request):
    states = get_doltdata('states')
    data_types = get_doltdata('data_types')
    format_types = get_doltdata('format_types')
    source_types = get_doltdata('source_types')
    update = get_doltdata('update_frequency')
    agency_types = get_doltdata('agency_types')
    context = {'states': states, 'data_types': data_types, 'format_types': format_types, 'source_types': source_types, 'update': update, 'agency_types': agency_types}
    return render(request, 'schema.html', context=context)

def get_agencies(request, state_iso):
    return JsonResponse(get_agencies_in_state(state_iso), safe=False)

def get_datasets(request, id):
    return JsonResponse(get_datasets_for_agency(id), safe=False)