from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import Case
from cart.forms import AddToCart

class CaseListView(ListView):
    queryset = Case.objects.filter(status='a')
    paginate_by = 6
    context_object_name = 'cases'
    template_name = 'cases/home.html'


class CaseDetailView(DetailView):
    model = Case
    template_name = 'cases/case_detail.html'
    context_object_name = 'case'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context['comment_form'] = ReviewForm()
        context['add_to_cart_form'] = AddToCart()
        return context


