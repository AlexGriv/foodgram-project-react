from django.urls import include, path
from rest_framework import routers

from .views import IngredientViewSet, RecipeViewSet, TagViewSet

router_v1 = routers.DefaultRouter()
router_v1.register(r'ingredients', IngredientViewSet)
router_v1.register(r'tags', TagViewSet)
router_v1.register(r'recipes', RecipeViewSet)

urlpatterns = [
    path('', include(router_v1.urls)),
]
