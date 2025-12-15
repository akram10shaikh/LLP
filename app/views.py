# project_malizia/app/views.py

from django.shortcuts import render
from .models import Section8
from rest_framework.decorators import api_view
from rest_framework.response import Response
# from app.chatbot.chatbot_processor import get_chatbot_response

def chunked(iterable, chunk_size):
    return [iterable[i:i + chunk_size] for i in range(0, len(iterable), chunk_size)]

def home_view(request):
    return render(request, 'home.html')

def section8_view(request):
    testimonials = Section8.objects.all()
    return render(request, 'section8.html', {'testimonials': testimonials})

def section10_view(request):
    return render(request, 'section10.html')

def about_view(request):
    return render(request, 'about.html')

def services_view(request):
    return render(request, 'services.html')

def services_detail(request):
    return render(request, 'services_detail.html')

def projects(request):
    return render(request, 'projects.html')

def clients(request):
    return render(request, 'clients.html')

def blog(request):
    return render(request, 'blog.html')

def careers(request):
    return render(request, 'careers.html')

def contact(request):
    return render(request, 'contact.html')

def outdoor_signage(request):
    return render(request, 'outdoor_signage.html')

def indoor_signage(request):
    return render(request, 'indoor_signage.html')

def project_detail(request, project_name):
    """View for individual project detail page"""
    from django.http import Http404
    
    # Project data dictionary
    projects_data = {
        'toyota': {
            'title': 'Toyota',
            'category': 'Outdoor Signage',
            'location': 'Dubai',
            'description': 'Toyota automobile showroom featuring comprehensive outdoor signage solution, including branded displays, directional signage, and illuminated exterior signage to enhance brand visibility and customer navigation. The project includes modern design elements that reflect Toyota\'s brand identity and corporate standards.',
            'gallery': [
                '/static/images/Toyota.png',
                '/static/images/Toyota2.png',
                '/static/images/Toyota3.png',
                '/static/images/Toyota4.png',
                '/static/images/Toyota.png',
                '/static/images/Toyota2.png',
                '/static/images/Toyota3.png',
                '/static/images/Toyota4.png',
                '/static/images/Toyota.png',
            ]
        },
        'chicory': {
            'title': 'Chicory',
            'category': 'Outdoor Signage',
            'location': 'Dubai',
            'description': 'Chicory retail project showcasing modern outdoor signage with vibrant branding elements. The signage solution combines contemporary design with functionality to attract customers and create a memorable brand experience.',
            'gallery': [
                'https://images.unsplash.com/photo-1552321554-5fefe8c9ef14?w=500&h=300&fit=crop',
                'https://images.unsplash.com/photo-1552321554-5fefe8c9ef14?w=500&h=300&fit=crop',
                'https://images.unsplash.com/photo-1552321554-5fefe8c9ef14?w=500&h=300&fit=crop',
                'https://images.unsplash.com/photo-1552321554-5fefe8c9ef14?w=500&h=300&fit=crop',
                'https://images.unsplash.com/photo-1552321554-5fefe8c9ef14?w=500&h=300&fit=crop',
                'https://images.unsplash.com/photo-1552321554-5fefe8c9ef14?w=500&h=300&fit=crop',
                'https://images.unsplash.com/photo-1552321554-5fefe8c9ef14?w=500&h=300&fit=crop',
                'https://images.unsplash.com/photo-1552321554-5fefe8c9ef14?w=500&h=300&fit=crop',
                'https://images.unsplash.com/photo-1552321554-5fefe8c9ef14?w=500&h=300&fit=crop',
            ]
        }
    }
    
    # Get project by name (case-insensitive)
    project = projects_data.get(project_name.lower())
    
    if not project:
        raise Http404("Project not found")
    
    return render(request, 'individual_project_page.html', {'project': project})

def digital_signage(request):
    return render(request, 'digital_signage.html')

def led_displays(request):
    return render(request, 'led_displays.html')

def vehicle_graphics(request):
    return render(request, 'vehicle_graphics.html')

def vinyl_stickers(request):
    return render(request, 'vinyl_stickers.html')

def large_format_printing(request):
    return render(request, 'large_format_printing.html')

def custom_acrylic_branding(request):
    return render(request, 'custom_acrylic_branding.html')

# Chatbot endpoint
@api_view(['POST'])
def chatbot_endpoint(request):
    try:
        user_message = request.data.get('message')
        
        if not user_message:
            return Response({
                'status': 'error',
                'message': 'No message provided'
            }, status=400)

        chatbot_response = get_chatbot_response(user_message)
        return Response({
            'status': 'success',
            'response': chatbot_response
        })

    except Exception as e:
        return Response({
            'status': 'error',
            'message': str(e)
        }, status=500)
