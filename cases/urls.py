from django.urls import path, re_path, include

from .views import CaseListView, CaseDetailView


urlpatterns = [
    path('', CaseListView.as_view(), name='case_list'),
    re_path(r'^case/(?P<slug>[-\w]+)/', CaseDetailView.as_view(), name='case_detail'),
]

