from django.shortcuts import render
from django.views.generic import ListView

from .models import Case


class CaseListView(ListView):
    queryset = Case.objects.filter(status='a')
    paginate_by = 6
    context_object_name = 'cases'
    template_name = 'cases/home.html'


