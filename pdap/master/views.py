from django.shortcuts import render
from django.http import HttpResponseRedirect

# for now, the root will just redirect to /map
def index(request):
    return HttpResponseRedirect("/map")