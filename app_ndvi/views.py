from typing import Any
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

# generic base view
from django.views.generic import TemplateView


class Ndvi(TemplateView):
    template_name = "efbrm.html"

    #def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        #return super().get_context_data(**kwargs)
     
    def get_context_data(self, **kwargs: Any) -> dict[str, Any]: 
        
        #return HttpResponse("Ndvi() view",  content_type="text/plain")
        return {"answer": "Ndvi() view"}