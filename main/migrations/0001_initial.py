# Generated by Django 4.2.4 on 2023-09-07 20:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='Почта')),
                ('full_name', models.CharField(max_length=150, verbose_name='ФИО')),
                ('comment', models.CharField(blank=True, max_length=400, null=True, verbose_name='Комментарий')),
            ],
            options={
                'verbose_name': 'Клиент',
                'verbose_name_plural': 'Клиенты',
                'ordering': ['full_name'],
            },
        ),
        migrations.CreateModel(
            name='Letter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, verbose_name='Заголовок')),
                ('body', models.TextField(blank=True, null=True, verbose_name='Содержание')),
            ],
            options={
                'verbose_name': 'Письмо',
                'verbose_name_plural': 'Письма',
                'ordering': ['title'],
            },
        ),
        migrations.CreateModel(
            name='MailingLog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(blank=True, choices=[('ok', 'Успешно'), ('failed', 'Ошибка')], max_length=20, null=True, verbose_name='Статус доставки рассылки')),
                ('datatime_last', models.DateTimeField(blank=True, null=True, verbose_name='Дата и время последней попытки')),
            ],
            options={
                'verbose_name': 'Лог',
                'verbose_name_plural': 'Логи',
            },
        ),
        migrations.CreateModel(
            name='Mailing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('period', models.CharField(choices=[('daily', 'Ежедневная'), ('weekly', 'Раз в неделю'), ('monthly', 'Раз в месяц')], max_length=20, verbose_name='Период жизни рассылки')),
                ('status', models.CharField(blank=True, choices=[('started', 'Запущена'), ('created', 'Создана'), ('done', 'Завершена')], max_length=20, null=True, verbose_name='Статус рассылки')),
                ('datatime_create', models.DateTimeField(verbose_name='Дата и время создание рассылки')),
                ('client', models.ManyToManyField(to='main.client', verbose_name='Клиент(ы), которому(-ым) отправлялось письмо')),
                ('letter', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='main.letter', verbose_name='Письмо, к рассылке')),
                ('mailing_log', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='main.mailinglog', verbose_name='Лог рассылки')),
            ],
            options={
                'verbose_name': 'Логика',
                'verbose_name_plural': 'Логика',
                'ordering': ['datatime_create'],
            },
        ),
    ]
