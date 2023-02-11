from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic

class Index(LoginRequiredMixin, generic.TemplateView):
    template_name = 'base/base.html'
    login_url="/admin"

