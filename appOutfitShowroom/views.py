from django.shortcuts import render
from django.shortcuts import get_object_or_404, get_list_or_404
from django.http import HttpResponse
from .models import Estilo, Ocasion, Outfit

#devuelve el listado de estilos
def index(request):
	#outfits = get_list_or_404(Estilo.objects.order_by('nombre'))
	#context = {'lista_outfits': outfits }
    #return render(request, 'nocobot/index.html', context)
	return render(request, 'nocobot/index.html')
	
	
