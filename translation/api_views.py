from rest_framework import viewsets
from rest_framework.generics import ListAPIView

from . import models
from . import serializers

class TranslationViewset(viewsets.ModelViewSet):
    queryset = models.Translation.objects.all()
    serializer_class = serializers.TranslationSerializer
    filterset_fields = ('word', 'id',)

class TranslationListView(ListAPIView):
    serializer_class = serializers.TranslationListSerializer
    queryset = models.Translation.objects.all()
