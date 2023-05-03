from django.urls import path
from about.views import AboutView

urlpatterns = [
    path('despre_noi/', AboutView.as_view(), name='despre-noi'),
]
