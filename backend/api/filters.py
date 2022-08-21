from django_filters.rest_framework import FilterSet, filters
from recipes.models import Recipe
from rest_framework.filters import SearchFilter


class RecipeFilter(FilterSet):
    tags = filters.AllValuesMultipleFilter(field_name='tags__slug')
    is_favorited = filters.BooleanFilter(method='get_is_favorited')
    is_in_shopping_cart = filters.BooleanFilter(
        method='get_is_in_shopping_cart'
    )

    def get_is_favorited(self, queryset, value, name):
        if value and not self.request.user.is_anonymous:
            return queryset.filter(favorited__user=self.request.user)
        return queryset

    def get_is_in_shopping_cart(self, queryset, value, name):
        if value and not self.request.user.is_anonymous:
            return queryset.filter(user_shopping_cart__user=self.request.user)
        return queryset

    class Meta:
        model = Recipe
        fields = ('author', 'tags')


class IngredientFilter(SearchFilter):
    search_param = 'name'
