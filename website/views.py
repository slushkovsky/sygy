from django.shortcuts import render
from django.views.decorators.http import require_http_methods


@require_http_methods(['GET', 'POST'])
def home(request): 
    if request.method == 'POST': 
        pass # TODO

    return render(request, 'home.html')
     
