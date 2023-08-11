from django.shortcuts import render, redirect
from .forms import ServiceRequestForm
from .models import ServiceRequest

def submit_service_request(request):
    if request.method == 'POST':
        form = ServiceRequestForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('request_tracking')
    else:
        form = ServiceRequestForm()
    return render(request, 'service_requests/submit_service_request.html', {'form': form})

def request_tracking(request):
    service_requests = ServiceRequest.objects.all()
    return render(request, 'service_requests/request_tracking.html', {'service_requests': service_requests})
