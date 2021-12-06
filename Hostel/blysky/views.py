from django.shortcuts import render
from django.views import View
from .models import *

# Create your views here.
class Body(View):
    def get(self, request):
        countries=Country.objects.all()
        context={'countries':countries}
        return render(request, 'body.html', context=context)

class SearchResults(View):
    def get(self, request):
        countries=Country.objects.all()
        hotels = Hotel.objects.filter(country=request.GET['countryWhere'])
        context={'countries':countries,
                'searchResults':hotels}
        return render(request, 'body.html', context=context)