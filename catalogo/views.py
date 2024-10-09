from rest_framework.filters import SearchFilter
from rest_framework import generics
from .models import Filme
from .serializers import FilmeSerializer
from django.http import HttpResponse

# View para listar e criar filmes
class FilmeListCreate(generics.ListCreateAPIView):
    queryset = Filme.objects.all()
    serializer_class = FilmeSerializer

# View para obter, atualizar e deletar um filme específico
class FilmeDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Filme.objects.all()
    serializer_class = FilmeSerializer



class FilmeListCreate(generics.ListCreateAPIView):
    queryset = Filme.objects.all()
    serializer_class = FilmeSerializer
    filter_backends = [SearchFilter]
    search_fields = ['genero']  # Isso permite a busca por gênero

