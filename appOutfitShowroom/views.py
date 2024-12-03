from django.shortcuts import render
from django.shortcuts import get_object_or_404, get_list_or_404
from django.http import HttpResponse
from .models import Estilo, Ocasion, Outfit

def index(request):
    #dame un outfit por estilo
    outfits = Outfit.objects.raw('''
        SELECT * FROM (
            SELECT * FROM appOutfitShowroom_Outfit 
            ORDER BY nombre ASC  -- Orden alfabético
        ) AS subquery
        GROUP BY estilo_id  -- Agrupamos por estilo para obtener solo un outfit por estilo
    ''')
#    outfits = Outfit.objects.all()[:8]  # Obtén solo los primeros 8 outfits
    return render(request, 'nocobot/index.html', {'outfits': outfits})

def lista_outfits(request):
    outfits = get_list_or_404(Outfit.objects.all())
    #poner list 404
    return render(request, 'nocobot/outfits.html', {'outfits': outfits})

# Vista para los detalles de un outfit
def detalle_outfit(request, outfit_id):
    outfit = get_object_or_404(Outfit, id=outfit_id)
    return render(request, 'nocobot/outfit.html', {'outfit': outfit})

# Vista para la lista de ocasiones
def lista_ocasiones(request):
    ocasiones = get_list_or_404(Ocasion.objects.all())
    return render(request, 'nocobot/ocasiones.html', {'ocasiones': ocasiones})

# Vista para los detalles de una ocasión
def detalle_ocasion(request, ocasion_id):
    ocasion = get_object_or_404(Ocasion, id=ocasion_id)
    outfits = ocasion.outfit_set.all()
    return render(request, 'nocobot/ocasion.html', {'ocasion': ocasion, 'outfits': outfits})

# Vista para la lista de estilos
def lista_estilos(request):
    estilos = get_list_or_404(Estilo.objects.all())
    return render(request, 'nocobot/estilos.html', {'estilos': estilos})

# Vista para los detalles de un estilo
def detalle_estilo(request, estilo_id):
    estilo = get_object_or_404(Estilo, id=estilo_id)
    outfits = estilo.outfit_set.all()
    return render(request, 'nocobot/estilo.html', {'estilo': estilo, 'outfits': outfits})

