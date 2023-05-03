from django.urls import path

from contact import views
# from contact.views import ContactCreateView


urlpatterns = [
     path('contact_us/', views.ContactCreateView.as_view(), name='contact-us'), #nume url = redirect-ul catre o alta pagina
]