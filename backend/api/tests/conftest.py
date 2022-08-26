import pytest

from recipes.models import AmountIngredient, Ingredient, Recipe, Tag
from users.models import User


@pytest.fixture
def user() -> User:
    user, _ = User.objects.get_or_create(
        username='TestUser',
        email='test@terst.test',
    )
    return user


@pytest.fixture
def tag() -> Tag:
    tag, _ = Tag.objects.get_or_create(
        name='Test Tag #1',
        color='ffffff',
        slug='test',
    )
    return tag


@pytest.fixture
def ingredient() -> Ingredient:
    ingredient, _ = Ingredient.objects.get_or_create(
        name='test',
        measurement_unit='test',
    )
    return ingredient


@pytest.fixture
def recipe(user, tag) -> Recipe:
    recipe, _ = Recipe.objects.get_or_create(
        author=user,
        name='Recipe #1',
        text='Test recipe',
        cooking_time=1,
    )
    recipe.tags.add(tag)
    return recipe


@pytest.fixture
def amount_ingredient(recipe, ingredient) -> AmountIngredient:
    ai, _ = AmountIngredient.objects.get_or_create(
        recipe=recipe,
        ingredient=ingredient,
        amount=1,
    )
    return ai
