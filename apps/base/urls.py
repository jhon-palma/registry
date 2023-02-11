from django.urls import path

from apps.base.views import Index

urlpatterns = [
    path('', Index.as_view(),name='index'),
]
