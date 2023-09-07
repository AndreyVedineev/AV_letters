from django.contrib import admin

from main.models import Client, Letter, Mailing


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'email', 'comment')
    list_filter = ('full_name',)
    search_fields = ('full_name',)
    verbose_name = 'Клиенты'


@admin.register(Letter)
class LetterAdmin(admin.ModelAdmin):
    list_display = ('title', 'body',)
    list_filter = ('title',)
    search_fields = ('title', 'body',)
    verbose_name = 'Письма'





@admin.register(Mailing)
class MailingAdmin(admin.ModelAdmin):
    list_display = ('period', 'status', 'datatime_create')
    list_filter = ('status',)
    search_fields = ('period', 'status',)
    verbose_name = 'Рассылка'

