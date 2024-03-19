from django import forms

from .models import Classification


class OrderCreateForm(forms.ModelForm):
    """ """
    name = forms.CharField(label='Название', widget=forms.TextInput(attrs={'class': 'form-input'}))

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
    scheme = forms.CharField(
        label="Схема подключения", widget=forms.FileInput(attrs={"class": "form-input"})
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
