import hashlib

from django.views.generic import TemplateView
from django.views.decorators.cache import never_cache
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Message, MessageSerializer
from .models import Md5, Md5Serializer

# Serve Vue Application
index_view = never_cache(TemplateView.as_view(template_name='index.html'))


class MessageViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows messages to be viewed or edited.
    """
    queryset = Message.objects.all()
    serializer_class = MessageSerializer


class Md5View(APIView):
    def get(self, request, format=None):
        md5_dict = request.query_params
        #print(md5_dict)
        type = md5_dict['type']
        key = md5_dict['key']
        if type == 'md5':
            m2 = hashlib.md5()
            m2.update(key.encode("utf-16le"))
            result = m2.hexdigest()
        return Response(result, status=status.HTTP_200_OK)


