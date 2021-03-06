# Хабр API

## Установка

1. Клонируем проект: `git clone git@github.com:artinnok/habr-api.git habr-api_project`
2. Переходим на уровень репозитория: `cd habr-api_project`
3. Ставим виртуальное окружение: `virtualenv -p python3 env`
4. Генерируем [секретный ключ](http://www.miniwebtool.com/django-secret-key-generator/).
5. Пропишем в *env/bin/activate*:
```bash
export SECRET_KEY='секретный ключ'
export DJANGO_SETTINGS_MODULE='config.settings.local'
```
6. Активируем виртуальное окружение: `source env/bin/activate`
7. Переходим на уровень проекта: `cd habr-api`
8. Поставим зависимости: `pip install -r requirements/local.txt`
9. Проводим миграции: `python manage.py migrate --settings config.settings.local`
10. Стартуем RabbitMQ: `rabbitmq-server`
11. Делаем пункты 6-7, в отдельном окне терминала стартуем Celery: `celery worker -A config.celery -l info`
12. Делаем пункты 6-7, в отдельном окне терминала стартуем сервер: `python manage.py runserver --settings config.settings.local`

## API
1. GET `/api/authors/` - список всех юзеров за сегодня
2. GET `/api/authors/<x>` - список постов юзера с primary key x
3. GET `/api/posts/<y>?word=hello` - получить tf_idf слова hello в посте с primary key y
