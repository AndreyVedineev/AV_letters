from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView

from main.forms import ClientForm
from main.models import Client, Letter
from main.serives import get_client_cache


class ClientListView(ListView):
    model = Client
    paginate_by = 10

    extra_context = {
        'title': 'Список клиентов'
    }

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        get_client_cache(context)
        return context


class ClientCreateView(CreateView):
    model = Client
    form_class = ClientForm
    success_url = reverse_lazy('main:client_list/')

    extra_context = {
        'title': 'Создание клиента'
    }


class ClientDetailView(DetailView):
    model = Client


class ClientUpdateView(UpdateView):
    model = Client
    form_class = ClientForm
    success_url = reverse_lazy('main:client_list/')

    extra_context = {
        'title': 'Редактирование  клиента'
    }


class ClientDeleteView(DeleteView):
    model = Client
    success_url = reverse_lazy('main:client_list/')


class LetterListView(ListView):
    model = Letter
    paginate_by = 3

    extra_context = {
        'title': 'Список писем'
    }

