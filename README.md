# Habr API

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
9. Стартуем RabbitMQ: `rabbitmq-server`
10. Делаем пункты 6-7, в отдельном окне терминала стартуем Celery: `celery
worker
 -A config
.celery -l info`
11. Делаем пункты 6-7, в отдельном окне терминала стартуем сервер: `python manage.py runserver
--settings config.settings.local`
