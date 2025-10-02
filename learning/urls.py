from django.urls import path
from  . import views

app_name='learning'

urlpatterns = [

    path('', views.Index, name='index'),
    path('home', views.home, name='home'), 
    path('verify/<int:transfer_id>/', views.verify, name='verify'),
    path('success/<int:transfer_id>/', views.success, name='success'),
    path('about',views.about, name='about'),
    path('services', views.services, name='services'),
    path('contactus', views.contact_view, name='contactus'),
    path('jani', views.jani, name='jani'),
    path('cbos', views.cbos, name='cbos'),
    path('partners',views.partners, name='partners'),
    path('corporate',views.corporate, name='corporate'),
    path('partners',views.small_screen_view, name='small_screen_view'),
    path('privacy',views.privacy, name='privacy'),
    path('disclaimer',views.disclaimer, name='disclaimer'),
]

