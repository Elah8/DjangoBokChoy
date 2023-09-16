from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name="home"),
    path('home.html', views.home, name="home"),
    path ('contact.html', views.contact, name="contact"),
    path('hours.html', views.hours, name="hours"),
    path('service.html', views.service, name="service"),
    path('fees.html', views.fees, name="fees"),
    path('downloadable.html', views.downloadable, name="downloadable"),
    path('policies.html', views.policies, name="policies"),
    path('resources.html', views.resources, name="resources"),
    path('clinicNews.html', views.clinicNews, name="clinicNews"),
    path('faqs.html', views.faqs, name="faqs"),
    path('about.html', views.about, name="about"),
    
    path('appointment.html', views.appointment, name="appointment"),
    

]
