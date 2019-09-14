from rest_framework import routers
from translation import api_views as translation_views

router = routers.DefaultRouter()
router.register(r'translation', translation_views.TranslationViewset)

