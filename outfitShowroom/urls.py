
"""
URL configuration for outfitShowroom project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls.i18n import i18n_patterns
from django.urls import path, include
from django.utils.translation import gettext_lazy as _
from django.conf import settings
from django.conf.urls.i18n import set_language
from django.conf.urls.i18n import i18n_patterns


urlpatterns = [
    path('i18n/', include('django.conf.urls.i18n')),
    path('', include('appOutfitShowroom.urls')),
    path('admin/', admin.site.urls),
]

urlpatterns += i18n_patterns(
    path('', include('appOutfitShowroom.urls')),  # Ajusta esto a tus URLs principales
)

urlpatterns += [
    path('', include('appOutfitShowroom.urls')),
]

admin.site.site_title = "Outfit Showroom site admin"
admin.site.site_header = "Outfit Showroom administration"
admin.site.index_title = "OutfitShowroom administration"

