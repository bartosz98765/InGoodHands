from django import forms
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


class DonationForm(ModelForm):
    categories = forms.ModelMultipleChoiceField(queryset=Category.objects.all(), widget=forms.CheckboxSelectMultiple())
    institution = forms.ModelChoiceField(queryset=Institution.objects.none())

    class Meta:
        model = Donation
        exclude = ('user',)

    # quantity = forms.IntegerField()
    # categories = forms.ModelMultipleChoiceField(queryset=Category.objects.all())
    # institution = forms.ModelChoiceField(queryset=Institution.objects.)
    # phone_number = models.CharField(max_length=12
    # city = models.CharField(max_length=24)
    # zip_code = models.CharField(max_length=6)
    # pick_up_date = models.DateField()
    # pick_up_time = models.TimeField()
    # pick_up_comment = models.CharField(max_length
    # user = models.ForeignKey(User, default=None,
