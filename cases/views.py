from django.shortcuts import render
from django.views.generic import ListView

def home_shower(request):
    return render(request, 'cases/home.html')


# class CaseListView(ListView):
#     # queryset = Case.objects.filter(active=True)
#     # paginate_by = 6
#     context_object_name = 'cases'
#     template_name = 'home.html'


