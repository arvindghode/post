from django.shortcuts import render, render_to_response, redirect
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin

class HomeView(LoginRequiredMixin, View):
    template_name = 'posts/index.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)