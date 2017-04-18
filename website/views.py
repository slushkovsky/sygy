from django.shortcuts import render
from django.views.decorators.http import require_http_methods, require_GET


@require_GET
def home(request): 
    return render(request, 'home.html')
     
@require_GET
def eye_guest(request): 
	return render(request, 'eye_guest.html')

@require_GET
def eye_wish(request): 
	return render(request, 'eye_wish.html')

@require_GET
def eye_service(request): 
	return render(request, 'eye_service.html')

@require_GET
def eye_merketer(request): 
	return render(request, 'eye_marketer.html')

@require_GET
def about_us(request): 
	return render(request, 'about_us.html')

@require_GET
def support(request): 
	return render(request, 'support.html')