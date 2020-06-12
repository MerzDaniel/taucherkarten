from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('nerd-area', views.nerdArea, name='nerd-area'),
    path('impressum', views.impressum, name='impressum'),
    path('datenschutz', views.dataProtection, name='data-protection'),
    path('see/<slug:lakeSlug>', views.lake, name='lakeBySlug'),
]