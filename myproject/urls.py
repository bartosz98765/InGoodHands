from django.contrib import admin
from django.urls import path
from ingoodhands import views
from ingoodhands.views import LandingPageView, AddDonationView, LoginView, LogoutView, RegisterView, ConfirmationView




urlpatterns = [
    path('admin/', admin.site.urls),
    path('', LandingPageView.as_view(), name='index'),
    path('adddonation/', AddDonationView.as_view(), name='adddonation-view'),
    path('confirmation/', ConfirmationView.as_view(), name='confirmation-view'),
    path('login/', LoginView.as_view(), name='login-view'),
    path('logout/', LogoutView.as_view(), name='logout-view'),
    path('register/', RegisterView.as_view(), name='register-view'),
    path('get_inst_by_cat/', views.get_inst_by_cat, name='get_inst_by_cat'),
]
