from itinerario.form import TaxiForm
from itinerario.models import Viaje, Taxi, Trabajador
from django.shortcuts import render
from django.views.generic import ListView, TemplateView, CreateView
from django.utils import timezone
# Create your views here.

class HomePageView(TemplateView):

    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context['latest_articles'] = Article.objects.all()[:5]
        return context
class ViajeListView(ListView):
    model = Viaje
    template_name  =  'itinerario/viajes_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context
class TaxiCreateView(CreateView):
    model = Taxi
    fields = ['nombre','capacidad','telefono','chofer','tipo']
    # form_cla = TaxiForm
    template_name = 'itinerario/create_taxi.html'
class ViajeCreateView(CreateView):
    model = Viaje
    fields = ['tipo_viaje','taxi','Trabajador','fecha','hora']
    template_name = 'itinerario/create_viaje.html'