from django.views.decorators.cache import cache_page

from main.apps import MainConfig
from django.urls import path

from main.views import *

app_name = MainConfig.name

urlpatterns = [
    path("", ClientListView.as_view(), name='client_list/'),
    path("client/create", ClientCreateView.as_view(), name='client_create/'),
    path("client/<int:pk>/detail/", ClientDetailView.as_view(), name='client_detail/'),
    path("client/<int:pk>/update/", ClientUpdateView.as_view(), name='client_update/'),
    path("client/<int:pk>/delete/", cache_page(60) (ClientDeleteView.as_view()), name='client_delete/'),

    path("letter", LetterListView.as_view(), name='letter_list/'),
    # path("letter/create", LetterCreateView.as_view(), name='letter_create/'),
    # path("letter/<int:pk>/detail/", LetterDetailView.as_view(), name='letter_detail/'),
    # path("letter/<int:pk>/update/", LetterUpdateView.as_view(), name='letter_update/'),
    # path("letter/<int:pk>/delete/", cache_page(60) (LetterDeleteView.as_view()), name='letter_delete/'),
    #



]