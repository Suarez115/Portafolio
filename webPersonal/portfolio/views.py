from django.shortcuts import render, get_object_or_404
from django.views.generic.detail import DetailView
from .models import Proyect, ProjectImage

# Create your views here.
def portfolio(request):
   proyects = Proyect.objects.all()
   projectImages = ProjectImage.objects.all()
   return render(request, 'portfolio/html/portfolio.html',{'proyects':proyects,
                                                           'proyectImg':projectImages})

class ImageProyectDetailView(DetailView):
     model = ProjectImage
     template_name =  'portfolio/html/portfolio.html'