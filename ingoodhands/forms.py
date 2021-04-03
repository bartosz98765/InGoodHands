from django import forms
from django.contrib.auth.hashers import check_password
from django.forms import ModelForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from ingoodhands.models import Category, Institution, Donation


def username_unique(username):
    if User.objects.filter(username=username):
        raise ValidationError('Użytkownik o takim emailu istnieje już w bazie.')


class RegisterForm(forms.Form):
    username = forms.CharField(min_length=3,
                               max_length=64,
                               widget=forms.EmailInput(attrs={'placeholder': 'Email'}),
                               validators=[username_unique])
    first_name = forms.CharField(min_length=3,
                                 widget=forms.TextInput(attrs={'placeholder': 'Imię'}),
                                 max_length=24)
    last_name = forms.CharField(min_length=3,
                                widget=forms.TextInput(attrs={'placeholder': 'Nazwisko'}),
                                max_length=30)
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Hasło'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Powtórz hasło'}))

    def clean(self):
        cleaned_data = super().clean()
        if cleaned_data['password1'] != cleaned_data['password2']:
            raise ValidationError('Hasła nie są takie same')


class LoginForm(forms.Form):
    username = forms.CharField(min_length=3,
                               max_length=64,
                               widget=forms.TextInput(attrs={'placeholder': 'Email'}))
    password = forms.CharField(min_length=8,
                               widget=forms.PasswordInput(attrs={'placeholder': 'Hasło'}))


class UserUpdateForm(ModelForm):
    username = forms.CharField(min_length=3, max_length=64, widget=forms.EmailInput())

    first_name = forms.CharField(min_length=3,
                                 widget=forms.TextInput(attrs={'placeholder': 'Imię'}),
                                 max_length=24)
    last_name = forms.CharField(min_length=3,
                                widget=forms.TextInput(attrs={'placeholder': 'Nazwisko'}),
                                max_length=30)
    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Podaj aktualne hasło'}))

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'confirm_password']

    def clean(self):
        cleaned_data = super(UserUpdateForm, self).clean()
        confirm_password = cleaned_data.get('confirm_password')
        if not check_password(confirm_password, self.instance.password):
            self.add_error('confirm_password', 'Błędne hasło')


class PasswordChangeForm(ModelForm):
    actual_password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': "Aktualne hasło"}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Nowe hasło'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Powtórz hasło'}))

    class Meta:
        model = User
        fields = ['actual_password', 'password', 'password2']

    def clean(self):
        cleaned_data = super(PasswordChangeForm, self).clean()
        actual_password = cleaned_data.get('actual_password')
        if not check_password(actual_password, self.instance.password):
            self.add_error('actual_password', 'Błędne hasło')
        if cleaned_data['password'] != cleaned_data['password2']:
            raise ValidationError('Hasła nie są takie same')


class DonationForm(ModelForm):
    institution = forms.ModelChoiceField(queryset=Institution.objects.all(), widget=forms.RadioSelect())

    class Meta:
        model = Donation
        exclude = ('user',)
        widgets = {
            'categories': forms.CheckboxSelectMultiple(),
            'quantity': forms.NumberInput(attrs={'min': 1, 'max': '60'}),
            'zip_code': forms.TextInput(),
            'phone_number': forms.TextInput(),
            'pick_up_date': forms.DateInput(attrs={'type': 'date'}),
            'pick_up_time': forms.TimeInput(attrs={'type': 'time'}),
            'pick_up_comment': forms.Textarea(attrs={'rows': 5}),
        }
