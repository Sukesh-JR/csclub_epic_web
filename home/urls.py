from home import views
from django.urls import path

urlpatterns = [
    path('', views.home, name='home-page'),
    path('team/', views.team, name='team-page'),
    path('contacts/', views.contact, name='contact-page'),
    path('timeline/', views.timeline, name='timeline-page'),
    path('event/', views.event, name='event-page'),
]