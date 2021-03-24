from django.shortcuts import render
from django.views import View


class LandingPageView(View):

    def get(self, request):
        ctx = {'title': 'HOME', 'header_template': 'ingoodhands/header.html'}
        return render(request, 'ingoodhands/index.html', ctx)


class AddDonationView(View):

    def get(self, request):
        ctx = {'title': 'DANATION', 'header_template': 'ingoodhands/header.html'}
        return render(request, 'ingoodhands/form.html', ctx)


class LoginView(View):

    def get(self, request):
        ctx = {'title': 'LOGIN', 'header_template': 'ingoodhands/header.html'}
        return render(request, 'ingoodhands/login.html', ctx)


class RegisterView(View):

    def get(self, request):
        ctx = {'title': 'REGISTER', 'header_template': 'ingoodhands/header.html'}
        return render(request, 'ingoodhands/register.html', ctx)
