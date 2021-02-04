from django.shortcuts import render
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import *
from .serializers import *
from django.shortcuts import get_object_or_404,get_list_or_404


# Create your views here.
class vehiculoView(APIView):
	def get(self, request):
		objL=vehiculo.objects.all()
		serializer_data=[]
		for obj in objL:	
			serializer=vehiculoSerializer(obj)
			serializer_data.append(serializer.data)	
		return Response(serializer_data)


	def delete(self, request, epc):
		obj=get_object_or_404(vehiculo, epc=epc)
		obj.delete()
		return Response({"estado":"ok"},status=status.HTTP_204_NO_CONTENT)


	def post(self, request, format=None):
		serializer = vehiculoSerializer(data = request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status= status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

	def patch(self, request, epc):
		obj=get_object_or_404(vechiculo, epc=epc)
		serializer = vehiculoSerializer(obj,data = request.data, partial=True)

		if serializer.is_valid():
			serializer.save()

		return Response(serializer.data)


class conductorView(APIView):
	def get(self, request):
		objL=conductor.objects.all()
		serializer_data=[]
		for obj in objL:	
			serializer=conductorSerializer(obj)
			serializer_data.append(serializer.data)	
		return Response(serializer_data)


	def delete(self, request, epc):
		obj=get_object_or_404(conductor, epc=epc)
		obj.delete()
		return Response({"estado":"ok"},status=status.HTTP_204_NO_CONTENT)


	def post(self, request, format=None):
		serializer = conductorSerializer(data = request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status= status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

	def patch(self, request, epc):
		obj=get_object_or_404(conductor, epc=epc)
		serializer = conductorSerializer(obj,data = request.data, partial=True)

		if serializer.is_valid():
			serializer.save()

		return Response(serializer.data)

class cajaView(APIView):
	def get(self, request):
		objL=caja.objects.all()
		serializer_data=[]
		for obj in objL:	
			serializer=cajaSerializer(obj)
			serializer_data.append(serializer.data)	
		return Response(serializer_data)


	def delete(self, request, epc):
		obj=get_object_or_404(caja, epc=epc)
		obj.delete()
		return Response({"estado":"ok"},status=status.HTTP_204_NO_CONTENT)


	def post(self, request, format=None):
		serializer = cajaSerializer(data = request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status= status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

	def patch(self, request, epc):
		obj=get_object_or_404(caja, epc=epc)
		serializer = cajaSerializer(obj,data = request.data, partial=True)

		if serializer.is_valid():
			serializer.save()

		return Response(serializer.data)


class registroView(APIView):
	def get(self, request):
		objL=registro.objects.all()
		serializer_data=[]
		for obj in objL:	
			serializer=registroSerializer(obj)
			serializer_data.append(serializer.data)	
		return Response(serializer_data)


	def delete(self, request, pk):
		obj=get_object_or_404(registro, pk=pk)
		obj.delete()
		return Response({"estado":"ok"},status=status.HTTP_204_NO_CONTENT)


	def post(self, request, format=None):
		serializer = registroSerializer(data = request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status= status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

	def patch(self, request, pk):
		obj=get_object_or_404(registro, pk=pk)
		serializer = registroSerializer(obj,data = request.data, partial=True)

		if serializer.is_valid():
			serializer.save()

		return Response(serializer.data)