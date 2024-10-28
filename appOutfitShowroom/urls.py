from django.contrib import admin
from django.urls import include, path
from . import views

urlpatterns = [
 path('appEmpresaDjango/', include('appEmpresaDjango.urls')),
 path('admin/', admin.site.urls),
]