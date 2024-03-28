from django import forms

from .models import Classification, TypeAVR, SmartRelay


class OrderCreateForm(forms.ModelForm):
    """ """
    name = forms.CharField(
        label='Название',
        widget=forms.TextInput(attrs={
            'class': 'form-input',
            'placeholder': 'Название шкафа'
            })
        )
    comment = forms.CharField(
        label="Комментарий",
        widget=forms.Textarea(attrs={
            "class": "form-input",
            "rows": 5,
            "cols": 80,
            'placeholder': 'Дополнительные требования'
            },
        ),
    )
    description = forms.CharField(
        label="Описание файла", widget=forms.FileInput(attrs={"class": "form-input"})
    )
    scheme = forms.CharField(
        label="Схема подключения", widget=forms.FileInput(attrs={"class": "form-input"})
    )

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.fields['type_avr'].empty_label = 'Выберите схему АВР'
        self.fields['relay'].empty_label = 'Выберите тип логического реле'
        self.fields['type_avr'].queryset = TypeAVR.objects.filter(access=True)
        self.fields['relay'].queryset = SmartRelay.objects.filter(access=True)

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
