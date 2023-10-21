from django.urls import path, include

from .views import CaseListView


urlpatterns = [
    path('', CaseListView.as_view(), name='case_list'),
]

