from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'map.html')

# get_agencies ajax is in the /intake folder