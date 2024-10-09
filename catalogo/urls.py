from django.urls import path
from . import views

urlpatterns = [
    path('filmes/', views.FilmeListCreate.as_view(), name='filters-list'),
    path('filmes/<int:pk>/', views.FilmeDetail.as_view(), name='filme-detail'),
    
]
