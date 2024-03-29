from django.contrib import admin

import api.constant
from .models import (AmountIngredient, FavoriteRecipe, Ingredient, Recipe,
                     ShoppingCart, Tag)


@admin.register(Ingredient)
class IngredientAdmin(admin.ModelAdmin):
    list_display = ('name', 'measurement_unit')
    list_filter = ('name',)
    empty_value_display = api.constant.EMPTY_VALUE_DISPLAY


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('name', 'color')
    empty_value_display = api.constant.EMPTY_VALUE_DISPLAY


class AmountIngredientInLine(admin.TabularInline):
    model = AmountIngredient


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = ('name', 'author')
    readonly_fields = ('number_additions_to_favorites',)
    list_filter = ('author', 'name', 'tags')
    list_per_page = 20
    inlines = [AmountIngredientInLine]
    empty_value_display = api.constant.EMPTY_VALUE_DISPLAY

    def number_additions_to_favorites(self, obj):
        return obj.favorite.count()


@admin.register(AmountIngredient)
class AmountIngredientAdmin(admin.ModelAdmin):
    list_display = (
        'recipe', 'ingredient', 'amount'
    )
    list_filter = ('recipe', 'ingredient')
    empty_value_display = api.constant.EMPTY_VALUE_DISPLAY


@admin.register(FavoriteRecipe)
class FavoriteRecipeAdmin(admin.ModelAdmin):
    list_display = ('user', 'recipe')
    list_filter = ('user', 'recipe')
    empty_value_display = api.constant.EMPTY_VALUE_DISPLAY


@admin.register(ShoppingCart)
class ShoppingCartAdmin(admin.ModelAdmin):
    list_display = ('user', 'recipe')
    list_filter = ('user', 'recipe')
    empty_value_display = api.constant.EMPTY_VALUE_DISPLAY
