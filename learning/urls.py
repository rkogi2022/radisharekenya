from django.urls import path
from  . import views

app_name='learning'

urlpatterns = [
    #prospects model urls
    path('', views.Index, name='index'),
    path('verify/<int:transfer_id>/', views.verify, name='verify'),
    path('success/<int:transfer_id>/', views.success, name='success'),
    path('about',views.about, name='about'),
    path('services', views.services, name='services'),
    path('contactus', views.contact_view, name='contactus'),
]

