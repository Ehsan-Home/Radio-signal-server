from django.http import JsonResponse
from .models import RadioModel
from .radioobject import RadioObject
from django.core import serializers
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view


@api_view(['POST'])
def add_radio(request):
    try:
        obj = RadioObject(request.data['type'], request.data['dispersion'],
                          request.data['right_ascension'], request.data['declination'])
        RadioModel.objects.create(**request.data).save()

        data = obj.payload()
        return Response(data, status=status.HTTP_201_CREATED)

    except:
        return Response("Input is not valid", status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def get_radio(request):
    data = RadioModel.objects.all()
    dataInSeri = serializers.serialize('json', data)

    return Response(dataInSeri, status=status.HTTP_200_OK)
