from .models import *
from rest_framework import serializers


class vehiculoSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = vehiculo
		fields = ('epc','placa')

class conductorSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = conductor
		fields = ('epc','nombre')

class cajaSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = caja
		fields = ('epc','id_caja')

class registroSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = registro
		fields = ('placa','nombre','id_caja','movimiento','estado','fecha')

#class registroSerializer(serializers.Serializer):
#	placa = serializers.CharField(required = True)
#	nombre = serializers.CharField(required = True)

