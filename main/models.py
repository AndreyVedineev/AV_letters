from django.db import models

NULLABLE = {'blank': True, 'null': True}


class Client(models.Model):
    email = models.EmailField(unique=True, verbose_name='Почта')
    full_name = models.CharField(max_length=150, verbose_name='ФИО')
    comment = models.CharField(max_length=400, **NULLABLE, verbose_name='Комментарий')

    class Meta:
        verbose_name = 'Клиент'  # Настройка для наименования одного объекта
        verbose_name_plural = 'Клиенты'  # Настройка для наименования набора объектов
        ordering = ['full_name']

    def __str__(self):
        return f'{self.email} - {self.full_name}'


class Letter(models.Model):
    title = models.CharField(max_length=150, verbose_name='Заголовок')
    body = models.TextField(**NULLABLE, verbose_name='Содержание')

    class Meta:
        verbose_name = 'Письмо'  # Настройка для наименования одного объекта
        verbose_name_plural = 'Письма'  # Настройка для наименования набора объектов
        ordering = ['title']

    def __str__(self):
        return f'{self.title} - {self.body}'


class MailingLog(models.Model):
    STATUS_OK = 'ok'
    STATUS_FAILED = 'failed'

    STATUSES = [(STATUS_OK, 'Успешно'),
                (STATUS_FAILED, 'Ошибка')]

    status = models.CharField(max_length=20, choices=STATUSES, **NULLABLE, verbose_name='Статус доставки рассылки')
    datatime_last = models.DateTimeField(auto_now=False,
                                         auto_now_add=False, **NULLABLE,
                                         verbose_name='Дата и время последней попытки')

    class Meta:
        verbose_name = 'Лог'  # Настройка для наименования одного объекта
        verbose_name_plural = 'Логи'  # Настройка для наименования набора объектов

    def __str__(self):
        return f'{self.status} - {self.datatime_last}'


class Mailing(models.Model):
    PERIOD_DAILY = 'daily'
    PERIOD_WEEKLY = 'weekly'
    PERIOD_MONTHLY = 'monthly'

    PERIODS = [(PERIOD_DAILY, 'Ежедневная'),
               (PERIOD_WEEKLY, 'Раз в неделю'),
               (PERIOD_MONTHLY, 'Раз в месяц'), ]

    STATUS_CREATED = 'created'
    STATUS_STARTED = 'started'
    STATUS_DONE = 'done'

    STATUSES = [(STATUS_STARTED, 'Запущена'),
                (STATUS_CREATED, 'Создана'),
                (STATUS_DONE, 'Завершена')]

    period = models.CharField(max_length=20, choices=PERIODS, verbose_name='Период жизни рассылки')
    status = models.CharField(max_length=20, choices=STATUSES, **NULLABLE, verbose_name='Статус рассылки')
    letter = models.OneToOneField(Letter, on_delete=models.CASCADE, verbose_name='Письмо, к рассылке')
    datatime_create = models.DateTimeField(auto_now=False, auto_now_add=False,
                                           verbose_name='Дата и время создание рассылки')
    client = models.ManyToManyField(Client, verbose_name='Клиент(ы), которому(-ым) отправлялось письмо')
    mailing_log = models.OneToOneField(MailingLog, on_delete=models.CASCADE, verbose_name='Лог рассылки')

    class Meta:
        verbose_name = 'Рассылка'  # Настройка для наименования одного объекта
        verbose_name_plural = 'Рассылки'  # Настройка для наименования набора объектов
        ordering = ['datatime_create']

    class Meta:
        verbose_name = 'Рассылка'  # Настройка для наименования одного объекта
        verbose_name_plural = 'Рассылки'  # Настройка для наименования набора объектов
        ordering = ['datatime_create']

    def __str__(self):
        return f'{self.period} - {self.status} - {self.letter} - {self.datatime_create} - {self.client} - {self.mailing_log}'
