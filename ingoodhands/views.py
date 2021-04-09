from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.core.paginator import Paginator
from django.shortcuts import render, redirect, reverse
from django.views import View
from django.views.generic import UpdateView
from ingoodhands.models import Donation, Institution
from ingoodhands.forms import RegisterForm, LoginForm, DonationForm, UserUpdateForm, PasswordChangeForm


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

    def post(self, request):
        form = DonationForm(request.POST)
        if form.is_valid():
            new_donation = form.save()
            new_donation.user = request.user
            new_donation.save()
            return redirect('confirmation-view')
        else:
            ctx = {'title': 'DANATION', 'header_template': 'ingoodhands/header.html', 'form': form}
            return render(request, 'ingoodhands/form.html', ctx)


class ConfirmationView(PermissionRequiredMixin, View):
    permission_required = 'ingoodhands.add_donation'

    def get(self, request):
        ctx = {'title': 'DANATION', 'header_template': 'ingoodhands/header.html'}
        return render(request, 'ingoodhands/confirmation.html', ctx)


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


class ProfileView(LoginRequiredMixin, View):

    def get(self, request):
        user = request.user
        user_donations = Donation.objects.filter(user=user).order_by('-pick_up_date')
        donation_true = []
        donation_false = []
        for el in user_donations:
            donation_true.append(el) if el.is_taken else donation_false.append(el)
        user_donations = donation_false + donation_true
        ctx = {'user_donations': user_donations, 'header_template': 'ingoodhands/header.html', 'user': user}
        return render(request, 'ingoodhands/profile.html', ctx)

    def post(self, request):
        donation = Donation.objects.get(pk=request.POST['is_taken'])
        donation.is_taken = not donation.is_taken
        donation.save()
        return redirect('profile-view')


class UserUpdateView(LoginRequiredMixin, UpdateView):
    model = User
    form_class = UserUpdateForm
    template_name = 'ingoodhands/update.html'

    def get_object(self, queryset=None):
        return self.request.user

    def get_success_url(self):
        return reverse('userupdate-view')

    def get_context_data(self, **kwargs):
        user = self.request.user
        userupdate_form = UserUpdateForm(instance=user)
        passwordchange_form = PasswordChangeForm()
        ctx = super(UserUpdateView, self).get_context_data(**kwargs)
        ctx['userupdate_form'] = userupdate_form
        ctx['passwordchange_form'] = passwordchange_form
        ctx['header_template'] = 'ingoodhands/header.html'
        return ctx


class PasswordChangeView(LoginRequiredMixin, UpdateView):
    model = User
    form_class = PasswordChangeForm
    template_name = 'ingoodhands/update.html'

    def get_object(self, queryset=None):
        return self.request.user

    def get_context_data(self, **kwargs):
        user = self.request.user
        userupdate_form = UserUpdateForm(instance=user)
        passwordchange_form = PasswordChangeForm()
        ctx = super(PasswordChangeView, self).get_context_data(**kwargs)
        ctx['userupdate_form'] = userupdate_form
        ctx['passwordchange_form'] = passwordchange_form
        ctx['header_template'] = 'ingoodhands/header.html'
        return ctx

    def form_valid(self, form):
        new_password = form.cleaned_data['password']
        if new_password != '':
            self.object.set_password(new_password)
        self.object.save()
        self.object = authenticate(username=self.object.username, password=new_password)
        login(self.request, self.object)
        return redirect('passwordchange-view')


def get_inst_by_cat(request):
    if request.user.has_perm('ingoodhands.add_donation'):
        inst_ids = request.GET.getlist('inst_ids')
        if inst_ids != []:
            institutions = []
            inst = Institution.objects.filter(categories__in=inst_ids)
            for el in set(inst):
                if inst.filter(pk=el.pk).count() == len(inst_ids):
                    institutions.append(el)
        else:
            institutions = []
        return render(request, 'ingoodhands/api_institutions.html', {'institutions': institutions})
    else:
        return redirect('login-view')