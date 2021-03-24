from django.contrib import admin
from django.urls import path
from ingoodhands.views import LandingPageView, AddDonationView, LoginView, RegisterView




urlpatterns = [
    path('admin/', admin.site.urls),
    path('', LandingPageView.as_view(), name='index'),
    path('adddonation/', AddDonationView.as_view(), name='adddonation-view'),
    path('login/', LoginView.as_view(), name='login-view'),
    path('register/', RegisterView.as_view(), name='register-view'),
]
