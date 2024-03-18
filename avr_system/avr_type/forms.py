from django import forms
from django.contrib.admin.sites import site
from django.contrib.admin.widgets import ForeignKeyRawIdWidget

from .models import Classification


class OrderCreateForm(forms.ModelForm):
    """ """

    # type_avr = forms.Select(attrs={'class': 'form-input'})
    name = forms.CharField(label='Название', widget=forms.TextInput(attrs={'class': 'form-input'}))
    # relay = forms.Select(attrs={'class': 'form-input'})
    # vnr = forms.CharField(label='Название', widget=forms.CheckboxInput(attrs={'class': 'form-input'}))
    # temp_tp = forms.CharField(label='Название', widget=forms.CheckboxInput(attrs={'class': 'form-input'}))
    # reset = forms.CharField(label='Название', widget=forms.CheckboxInput(attrs={'class': 'form-input'}))
    # choice_in = forms.CharField(label='Название', widget=forms.CheckboxInput(attrs={'class': 'form-input'}))
    # dgu = forms.CharField(label='Название', widget=forms.CheckboxInput(attrs={'class': 'form-input'}))
    # work_tp = forms.CharField(label='Название', widget=forms.CheckboxInput(attrs={'class': 'form-input'}))
    # status_box = forms.CharField(label='Название', widget=forms.CheckboxInput(attrs={'class': 'form-input'}))
    # signal_ozz = forms.CharField(label='Название', widget=forms.CheckboxInput(attrs={'class': 'form-input'}))
    # lamp_avr_ready = forms.CharField(label='Название', widget=forms.CheckboxInput(attrs={'class': 'form-input'}))
    # lamp_avr_work = forms.CharField(label='Название', widget=forms.CheckboxInput(attrs={'class': 'form-input'}))
    comment = forms.CharField(
        label="Комментарий",
        widget=forms.Textarea(attrs={
            "class": "form-input",
            "rows": 5,
            "cols": 80,
            'placeholder': 'Здесь можете ...'
            },
        ),
    )
    description = forms.CharField(
        label="Описание файла", widget=forms.FileInput(attrs={"class": "form-input"})
    )

    class Meta:
        model = Classification
        fields = [
            "type_avr",
            "name",
            "relay",
            "vnr",
            "temp_tp",
            "reset",
            "choice_in",
            "dgu",
            "work_tp",
            "status_box",
            "signal_ozz",
            "lamp_avr_ready",
            "lamp_avr_work",
            "comment",
        ]
