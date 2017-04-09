from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from snippets.models import Snippet
from snippets.serializers import SnippetSerializer, SystemSummarySerializer, SystemStateSerializer, SystemStateSerializerCustom
import logging, logging.handlers
from snippets.models import SystemOverview, SystemState
from django.core import serializers
from django.forms.models import model_to_dict
import json
from django.http import HttpResponse



logging.basicConfig(level=logging.DEBUG)

@api_view(['GET'])
def snippet_list(request, format=None):
    """
    List all snippets
    """
    if request.method == 'GET':
        snippets = Snippet.objects.all()
        serializer = SnippetSerializer(snippets, many=True)
        return Response(serializer.data)

@api_view(['GET'])
def snippet_detail(request, pk, format=None):
    """
    Retrieve a snippet instance.
    """
    # logging.info("getting snippet_detail")
    # params = request.GET
    # logging.info(request.GET)
    # logging.info("these are the parameters!")
    # for i in params.items():
    #     logging.info(i[0])
    #     logging.info(i[1])
    #
    # logging.info("exit for")

    try:
        # snippet = Snippet.objects.get(pk=pk)
        snippet = Snippet.objects.filter(code__startswith=pk)
    except Snippet.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = SnippetSerializer(snippet, many=True)
        return Response(serializer.data)

    # my_model = SystemState.objects.filter(pk=pk)
    # response = serializers.serialize("json", my_model, many=True)
    # return HttpResponse(response, content_type='application/json')


@api_view(['GET'])
def systemsummary(request, pk, format=None):
    """
    Retrieve a snippet instance.
    """
    # logging.info("getting system summary with %s", pk)
    # params = request.GET
    # logging.info(request.GET)
    # logging.info("these are the parameters!")
    # for i in params.items():
    #     logging.info(i[0])
    #     logging.info(i[1])
    #
    # logging.info("exit for")

    try:
        obj = SystemOverview.objects.filter(serial=pk)
    except SystemOverview.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = SystemSummarySerializer(obj, many=True)
        return Response(serializer.data)
        # return Response(serializers.serialize("json", obj))

        # return Response(json.dumps(list(obj), indent=4))


@api_view(['GET'])
def systemstates(request, pk, format=None):
    """
    Retrieve a snippet instance.
    """

    logging.info("getting system states with %s", pk)
    params = request.GET
    logging.info(request.GET)
    logging.info("these are the parameters!")
    count = 0
    for i in params.items():
        count += 1
        logging.info(i[0])
        logging.info(i[1])

    logging.info("exit for")

    if count > 0:
        obj = SystemState.objects.filter(systemId=pk)
        logging.info(obj)
        # response = serializers.serialize("json", list(obj), fields=('from_date'))
        # return HttpResponse(response, content_type='application/json')
        serializer = SystemStateSerializerCustom(obj, many=True)
        return Response(serializer.data)


    # try:
    #     # snippet = Snippet.objects.get(pk=pk)
    #     obj = SystemState.objects.filter(systemId=pk)
    # except SystemState.DoesNotExist:
    #     return Response(status=status.HTTP_404_NOT_FOUND)
    #
    # if request.method == 'GET':
    #     return Response(serializers.serialize("json", [obj,]))

    try:
        obj = SystemState.objects.filter(systemId=pk)
    except SystemState.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = SystemStateSerializer(obj, many=True)
        return Response(serializer.data)

    # my_model = SystemState.objects.filter(systemId=pk)
    # response = serializers.serialize("json", my_model)
    # return HttpResponse(response, content_type='application/json')
