from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'basic_appt/index.html')

def other(request):
    return render(request, 'basic_appt/other.html')

def relative(request):
    return render(request, 'basic_appt/relative_url_templates.html')
