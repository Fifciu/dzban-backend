from rest_framework import viewsets
from rest_framework.generics import ListAPIView
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK

from . import models
from . import serializers

class TranslationViewset(viewsets.ModelViewSet):
    queryset = models.Translation.objects.all()
    serializer_class = serializers.TranslationSerializer
    filterset_fields = ('word', 'id',)

    @action(methods=["get"], detail=False, url_path='get-words')
    def get_words(self, request, *args, **kwargs):
        words = request.GET['words']
        words = words.split()
        result = []
        for word in words:
            try:
                word_ = models.Translation.objects.filter(word=word).first()
            except:
                word_ = None
            if word_:
                result.append({"word":word_.word, "meaning": word_.meaning, "example": word_.example})

        return Response(result, HTTP_200_OK)




class TranslationListView(ListAPIView):
    serializer_class = serializers.TranslationListSerializer
    queryset = models.Translation.objects.all()

