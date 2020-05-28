from django.urls import path
from . import views
from .views import ArticoliView,GiornalistiView, ArticoliGiornalistiView


app_name = 'news'
urlpatterns = [
    path('', views.home, name='home'),
    
    path('lista-articoli', ArticoliView.as_view(), name='articoli'),
    path('lista-giornalisti', GiornalistiView.as_view(), name='giornalisti'),
    path('lista-articoli/<int:pk>', ArticoliGiornalistiView, name='articoli'),
]