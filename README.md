[![Foodgram Actions Status](https://github.com/AlexGriv/yamdb_final/workflows/CI/badge.svg)](https://github.com/AlexGriv/yamdb_final/actions)
# Проект Foodgram.

## Технологии
* Python
* Django
* Django REST Framework
* django-filter
* Docker

## Как запустить проект
Клонировать репозиторий:
```
https://github.com/AlexGriv/foodgram-project-react.git
```
Проверьте разрешения доступа к папке Docker'у:
```
Open Docker and follow this -> settings ->Resources ->
FileSharing. Add required folder and hit Apply & Restart
```
Собрать и запустить:
```
docker-compose up -d --build из папки ./infra
```
Выполните по очереди команды:
```
docker-compose exec web python manage.py migrate
docker-compose exec web python manage.py createsuperuser
docker-compose exec web python manage.py collectstatic --no-input
```
Проверка:
```
зайти на http://localhost/admin/
```
Шаблон наполнения env-файла:
```
DB_ENGINE=django.db.backends.postgresql # указываем, что работаем с postgresql
DB_NAME=postgres # имя базы данных
POSTGRES_USER=postgres # логин для подключения к базе данных
POSTGRES_PASSWORD=postgres # пароль для подключения к БД (установите свой)
DB_HOST=db # название сервиса (контейнера)
DB_PORT=5432 # порт для подключения к БД
SECRET_KEY = ''
ALLOWED_HOSTS=example.com
