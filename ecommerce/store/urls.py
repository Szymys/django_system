from django.urls import path

from . import views

urlpatterns = [
    
    # STRONA GLOWNA
    path('', views.store, name='store'),

]





