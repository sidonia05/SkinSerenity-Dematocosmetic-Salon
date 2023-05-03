from django.views.generic import TemplateView

class HomeView(TemplateView):
    template_name = 'home/homepage.html'  # din fisierul home, homepage.html