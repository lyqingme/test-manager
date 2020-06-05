from django.db import models
from rest_framework import serializers


class Message(models.Model):
    subject = models.CharField(max_length=200)
    body = models.TextField()


class MessageSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Message
        fields = ('url', 'subject', 'body', 'pk')


class Md5(models.Model):
    """
    """
    Md5 = models.CharField(max_length=100)
    Md5_str = models.CharField(max_length=200)


class Md5Serializer(serializers.HyperlinkedModelSerializer):
    """
    """
    class Meta:
        model = Md5
        fields = ('Md5', 'Md5_str')
