from rest_framework import serializers
from clientes.models import Cliente
from clientes.validators import *


class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'
    def validate(self, data):
        if not cpf_valido(data['cpf']):
            raise serializers.ValidationError({'cpf':'O CPF deve conter 11 dígitos!'}) 
        if not nome_valido(data['nome']):
            raise serializers.ValidationError({'nome':'Este campo deve conter somente caracteres alfabéticos'})
        if not rg_valido(data['rg']):
            raise serializers.ValidationError({'rg':'O RG de conter 9 dígitos'})
        if not telefone_valido(data['celular']):
            raise serializers.ValidationError({'celular':'Telefone inválido.'})
        return data

    