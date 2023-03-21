from django.urls import path
from . import views

urlpatterns = [
    path('hello/', views.hello),
    path('translate/', views.translate),
    path('translate-page/', views.translate_page),
]
