# project_malizia/app/urls.py

from django.urls import path
from . import views

urlpatterns = [
    # Your existing paths
    path('', views.home_view, name='home'),
    path('section8/', views.section8_view, name='section8'),
    path('section10/', views.section10_view, name='section10'),
    path('about/', views.about_view, name='about'),
    path('services/', views.services_view, name='services'),
    # Specific service paths - MUST come before generic slug pattern
    path('services/outdoor-signage/', views.outdoor_signage, name='outdoor_signage'),
    path('services/indoor-signage/', views.indoor_signage, name='indoor_signage'),
    path('services/digital-signage/', views.digital_signage, name='digital_signage'),
    path('services/led-displays/', views.led_displays, name='led_displays'),
    path('services/vehicle-graphics/', views.vehicle_graphics, name='vehicle_graphics'),
    path('services/vinyl-stickers/', views.vinyl_stickers, name='vinyl_stickers'),
    path('services/large-format-printing/', views.large_format_printing, name='large_format_printing'),
    path('services/custom-acrylic-branding/', views.custom_acrylic_branding, name='custom_acrylic_branding'),
    # Generic slug pattern - comes after specific paths
    path('services/<slug:slug>/', views.services_detail, name='service_detail'),
    path('project/<str:project_name>/', views.project_detail, name='project_detail'),
    path('projects/', views.projects, name='projects'),
    path('clients/', views.clients, name='clients'),
    path('blog/', views.blog, name='blog'),
    path('careers/', views.careers, name='careers'),
    path('contact/', views.contact, name='contact'),
    
    # Add the new chatbot endpoint
    path('api/chatbot/', views.chatbot_endpoint, name='chatbot_endpoint'),  # new
]
