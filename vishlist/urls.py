from django.urls import path
from . import views

urlpatterns = [
    path('', views.customize_view, name='customize'),
    path('login_signup/', views.login_signup, name='login_signup'),  
    path('home/', views.home, name='home'),  
    path('forgot_password/', views.forgot_password, name='forgot_password'), 
    path('categories/', views.categories_page, name='categories_page'),   

   
]
