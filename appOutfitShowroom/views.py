from django.shortcuts import render
from django.shortcuts import get_object_or_404, get_list_or_404
from django.http import HttpResponse
from .models import Estilo, Ocasion, Outfit

def index(request):
    #return HttpResponse("Listado de outfits")
	return render(request, 'nocobot/index.html')
	
