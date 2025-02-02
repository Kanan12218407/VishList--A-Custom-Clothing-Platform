from pyexpat.errors import messages
from django.shortcuts import redirect, render
from .models import Fabric, Button
from django.contrib import messages
from .models import Fabric, EmbroideryDesign, Button

def customize_view(request):
    fabrics = Fabric.objects.all()
    buttons = Button.objects.all()
    context = {
        'fabrics': fabrics,
        'buttons': buttons,
    }
    return render(request, 'vishlist/customise.html', context)

def login_signup(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        password = request.POST.get('password')
        
        # Process the data, e.g., save to database, authenticate, etc.
        # Example: Just printing for demonstration
        print(f'Name: {name}, Email: {email}, Phone: {phone}, Password: {password}')
        
        # Redirect to a new page or render a success message
        messages.success(request, 'You have successfully signed up!')
        return redirect('login_signup')
    
    return render(request, 'vishlist/login_signup.html')
def home(request):
    return render(request, 'vishlist/home.html')
def forgot_password(request):
    return render(request, 'vishlist/forgot_password.html')

def customize_views(request):
    fabrics = Fabric.objects.all()
    designs = EmbroideryDesign.objects.all()
    buttons = Button.objects.all()
    return render(request, 'customization/customize.html', {
        'fabrics': fabrics,
        'designs': designs,
        'buttons': buttons,
    })
def categories_page(request):
    return render(request, 'vishlist/categories.html')