from django.shortcuts import render
from django.views import View



class GraficoFaturamento(View):
    
    def get(self, request, *args, **kwargs):
        context = {

        }
        return render(request, 'graficos/grafico_faturamento.html', context)
    def post(self, request, *args, **kwargs):
        pass