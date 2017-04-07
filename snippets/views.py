from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from snippets.models import Snippet
from snippets.serializers import SnippetSerializer
import logging, logging.handlers

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
    logging.info("getting snippet_detail")
    params = request.GET
    logging.info(request.GET)
    logging.info("these are the parameters!")
    for i in params.items():
        logging.info(i[0])
        logging.info(i[1])

    logging.info("exit for")

    try:
        # snippet = Snippet.objects.get(pk=pk)
        snippet = Snippet.objects.get(code__startswith=pk)
    except Snippet.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = SnippetSerializer(snippet)
        return Response(serializer.data)
