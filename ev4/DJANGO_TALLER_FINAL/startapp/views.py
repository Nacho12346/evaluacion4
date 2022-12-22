from django.shortcuts import render, redirect
from startapp.models import Inscritos, Institucion
from startapp.forms import FormInscritos
from django.http import JsonResponse
from .serializers import InscritosSerializer, InstitucionSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from django.http import Http404

#crud

def index(request):
    return render(request, 'index.html')

def listar(request):
    ins = Inscritos.objects.all()
    data = {'Inscritos': ins}
    return render(request, 'listar.html', data)

def agregar(request):
    form = FormInscritos()
    if request.method == 'POST':
        form = FormInscritos(request.POST)
        if form.is_valid():
            form.save()
        return index(request)
    data = {'form' : form}
    return render(request, 'agregar.html', data)

def eliminar(request, id):
    ins = Inscritos.objects.get(id = id)
    ins.delete()
    return redirect('/inscripciones')

def actualiza(request, id):
    ins = Inscritos.objects.get(id = id)
    form = FormInscritos(instance=ins)
    if request.method == 'POST':
        form = FormInscritos(request.POST, instance=ins)
        if form.is_valid():
            form.save()
        return index(request)
    data = {'form': form}
    return render(request, 'agregar.html', data)


def Api(request):
    inscritos = Inscritos.objects.all()
    data = {'inscritos' : list(inscritos.values('id', 'nombreCompleto', 'telefono', 'fechainscripcion', 'institucion', 'horainscripcion', 'estados', 'observacion'))}

    return JsonResponse(data)

class ListarCBV(APIView):

    def get(self, request):
        estu = Inscritos.objects.all()
        serial = InscritosSerializer(estu, many=True)
        return Response(serial.data)

    def post(self, request):
        serial = InscritosSerializer(data = request.data)
        if serial.is_valid():
            serial.save()
            return Response(serial.data, status=status.HTTP_201_CREATED)
        return Response(serial.errors, status=status.HTTP_400_BAD_REQUEST)
    
class DetalleCBV(APIView):

    def get_object(self, pk):
        try:
            return Inscritos.objects.get(pk=pk)
        except Inscritos.DoesNotExist:
            return Http404
        
    def get(self, request, pk):
        estu = self.get_object(pk)
        serial = InscritosSerializer(estu)
        return Response(serial.data)

    def put(self, request, pk):
        estu = self.get_object(pk)
        serial = InscritosSerializer(estu, data=request.data)
        if serial.is_valid():
            serial.save()
            return Response(serial.data)
        return Response(serial.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        estu = self.get_object(pk)
        estu.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST'])
def ListarFBV(request):
    if request.method == 'GET':
        estu = Institucion.objects.all()
        serial = InstitucionSerializer(estu, many=True)
        return Response(serial.data)
    
    if request.method == 'POST':
        serial = InstitucionSerializer(data = request.data)
        if serial.is_valid():
            serial.save()
            return Response(serial.data, status=status.HTTP_201_CREATED)
        return Response(serial.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def DetalleFBV(request, pk):
    try:
        estu = Institucion.objects.get(id = pk)
    except Institucion.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serial = InstitucionSerializer(estu)
        return Response(serial.data)

    if request.method == 'PUT':
        serial = InstitucionSerializer(estu, data=request.data)
        if serial.is_valid():
            serial.save()
            return Response(serial.data)
        return Response(serial.errors, status=status.HTTP_400_BAD_REQUEST)
        
    if request.method == 'DELETE':
        estu.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)