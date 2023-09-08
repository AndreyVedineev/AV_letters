from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django import forms
from django.urls import reverse_lazy

from main.models import Client, Letter


class StyleFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class ClientForm(StyleFormMixin, forms.ModelForm):
    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.helper = FormHelper(self)
    #     self.helper.form_action = reverse_lazy('shop:flowers_list/')

    class Meta:
        model = Client
        fields = '__all__'

    def clean_name(self):
        bad = {'козел', 'дурак', 'крипта', 'биржа', 'бесплатно', 'обман', 'полиция',
               'радар'}
        cleaned_data = self.cleaned_data['full_name']
        words_name = cleaned_data.lower().split()
        if bad & set(words_name):
            raise forms.ValidationError(f'У нас запрешеннно использовать слова - {bad}')

        return cleaned_data


class LetterForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Letter
        fields = '__all__'
