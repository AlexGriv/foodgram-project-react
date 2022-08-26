import pytest
from django.urls import reverse
from rest_framework.test import APIClient

from ..serializers import RecipePostSerializer
from recipes.models import Recipe


@pytest.mark.django_db
def test_recipe_post_serializer(user, ingredient, tag, rf):
    """ Проверяем сериализатор """
    # Данные из спецификации
    data = {
        "ingredients": [
            {
                "id": ingredient.id,
                "amount": 10
            }
        ],
        "tags": [tag.id],
        "image": "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAABAgMAAABieywaAAAACVBMVEUAAAD///9fX1/S0ecCAAAACXBIWXMAAA7EAAAOxAGVKw4bAAAACklEQVQImWNoAAAAggCByxOyYQAAAABJRU5ErkJggg==",
        "name": "TEST",
        "text": "string",
        "cooking_time": 1
    }
    # Подготовим request для передачи его в контексте
    request = rf.post('')
    request.user = user
    # Инициализируем сериализатор
    serializer = RecipePostSerializer(
        data=data,
        context={'request': request}
    )
    # Проверяем, что сериализатор распарсил входные данные по спеке
    serializer.is_valid(raise_exception=True)
    # проверяем, что данные распарсились
    # assert serializer.data is not None
    # Проверяем, что до момента сохранения сериализатора объекта в БД не было
    assert Recipe.objects.count() == 0
    # Проверяем, что сериализатор может создать объект
    recipe: Recipe = serializer.save()
    # Проверяем, что объект успешно создался
    assert Recipe.objects.count() == 1
    # Проверяем, что сохранились нужные данные
    assert recipe.name == data['name']


@pytest.mark.django_db
def test_recipe_view(user, ingredient, tag):
    client = APIClient()
    client.force_authenticate(user=user)
    url = reverse('recipe-list')
    payload = {
        "ingredients": [
            {
                "id": ingredient.id,
                "amount": 10
            },
        ],
        "tags": [tag.id],
        "image": "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAABAgMAAABieywaAAAACVBMVEUAAAD///9fX1/S0ecCAAAACXBIWXMAAA7EAAAOxAGVKw4bAAAACklEQVQImWNoAAAAggCByxOyYQAAAABJRU5ErkJggg==",
        "name": "TEST",
        "text": "string",
        "cooking_time": 1
    }
    response = client.post(url, data=payload, format='json')
    assert response.status_code == 201, response.data
