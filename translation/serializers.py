from rest_framework import serializers
from translation import models

class TranslationSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Translation
        fields = ('id', 'word', 'meaning', 'example')

class TranslationListSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Translation
        fields = ('id', 'word',)
