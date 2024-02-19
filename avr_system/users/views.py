from typing import Any
from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import Profile


class ProfileDetailView(ListView):
    """
    
    """
    model = Profile
    template_name = 'profile/account.html'
    context_object_name = 'profile'

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context.update(
            title='Профиль'
        )
        return context
