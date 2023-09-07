from django.conf import settings
from django.core.cache import cache

from main.models import Client


def get_client_cache(context):
    if settings.CACHE_ENABLED:
        # Проверяем включенность кеша
        key = 'client_list'  # Создаем ключ для хранения
        client_list = cache.get(key)  # Пытаемся получить данные
        if client_list is None:
            # Если данные не были получены из кеша, то выбираем из БД и записываем в кеш
            client_list = Client.objects.all()
            cache.set(key, client_list)
    else:
        # Если кеш не был подключен, то просто обращаемся к БД
        client_list = Client.objects.all()

    context['category_list'] = client_list

    return context
