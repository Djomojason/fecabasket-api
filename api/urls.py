from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ClubViewSet, EntraineurViewSet, JoueurViewSet, OfficielViewSet

router = DefaultRouter()
router.register(r'clubs', ClubViewSet)
router.register(r'entraineurs', EntraineurViewSet)
router.register(r'joueurs', JoueurViewSet)
router.register(r'officiels', OfficielViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
