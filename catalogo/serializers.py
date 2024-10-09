from rest_framework import serializers
from .models import Filme

class FilmeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Filme
        fields = '__all__'

    # Validação customizada para o campo 'ano'
    def validate_ano(self, value):
        if value < 1888 or value > 2024:
            raise serializers.ValidationError("O ano deve estar entre 1888 e 2024.")
        return value
