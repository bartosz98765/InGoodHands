from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.views import View
from ingoodhands.models import Donation, Institution, Category
from ingoodhands.forms import RegisterForm, LoginForm, DonationForm


class LandingPageView(View):

    def get(self, request):
        user = request.user

        institutions = Institution.objects.all()
        donations = Donation.objects.all()
        foundations_list = institutions.filter(type='FOUND')
        organizations = institutions.filter(type='ORG')
        locals = institutions.filter(type='LOCAL')

        paginator_found = Paginator(foundations_list, 6)
        page_found = request.GET.get('page')
        foundations = paginator_found.get_page(page_found)
        list_of_pagenumbers = [i for i in range(1, foundations.paginator.num_pages + 1)]

        ctx = {'title': 'HOME',
               'header_template': 'ingoodhands/header.html',
               'bags_quantity': sum([el.quantity for el in donations]),
               'institutions_quantity': len(list(set([r.institution for r in donations]))),
               'foundations': foundations,
               'organizations': organizations,
               'locals': locals,
               'list_of_pagenumbers': list_of_pagenumbers,
               'user': user
               }
        return render(request, 'ingoodhands/index.html', ctx)


class AddDonationView(PermissionRequiredMixin, View):
    permission_required = 'ingoodhands.add_donation'

    def get(self, request):
        form = DonationForm()
        ctx = {'title': 'DANATION', 'header_template': 'ingoodhands/header.html', 'form': form}
        return render(request, 'ingoodhands/form.html', ctx)


class LoginView(View):

    def get(self, request):
        form = LoginForm()
        ctx = {'title': 'LOGIN', 'header_template': 'ingoodhands/header.html', 'form': form}
        return render(request, 'ingoodhands/login.html', ctx)

    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                return redirect('index')
            elif User.objects.filter(username=username):
                ctx = {'title': 'REGISTER',
                       'header_template': 'ingoodhands/header.html',
                       'form': form,
                       'error': 'Błędne hasło'}
                return render(request, 'ingoodhands/login.html', ctx)
            else:
                return redirect('register-view')
        ctx = {'title': 'LOGIN', 'header_template': 'ingoodhands/header.html', 'form': form}
        return render(request, 'ingoodhands/login.html', ctx)


class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('index')


class RegisterView(View):

    def get(self, request):
        form = RegisterForm()
        ctx = {'title': 'REGISTER', 'header_template': 'ingoodhands/header.html', 'form': form}
        return render(request, 'ingoodhands/register.html', ctx)

    def post(self, request):
        form = RegisterForm(request.POST)
        if form.is_valid():
            User.objects.create_user(
                username=form.cleaned_data['username'],
                first_name=form.cleaned_data['first_name'],
                last_name=form.cleaned_data['last_name'],
                password=form.cleaned_data['password1'],
            )
            return redirect('login-view')
        else:
            ctx = {'title': 'REGISTER', 'header_template': 'ingoodhands/header.html', 'form': form}
            return render(request, 'ingoodhands/register.html', ctx)


def get_inst_by_cat(request):
    inst_ids = request.GET.getlist('inst_ids')
    if inst_ids != []:
        institutions = Institution.objects.filter(categories__in=inst_ids).distinct()
    else:
        institutions = []
    return render(request, 'ingoodhands/api_institutions.html', {'institutions': institutions})
