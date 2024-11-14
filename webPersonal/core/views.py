from django.shortcuts import render, HttpResponse

# Create your views here.
def home(request):
    return render(request, 'core/html/home.html')

def about(request):
    return render(request, 'core/html/about.html')

def contact(request):
   return render(request, 'core/html/contact.html')


