from django.contrib import admin
from django.urls import path
from ingoodhands import views
from ingoodhands.views import (LandingPageView, AddDonationView, LoginView, LogoutView,
                               RegisterView, ConfirmationView, ProfileView, UserUpdateView,
                               PasswordChangeView, ChangeView)




urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),
    path('', LandingPageView.as_view(), name='index'),
    path('adddonation/', AddDonationView.as_view(), name='adddonation-view'),
    path('confirmation/', ConfirmationView.as_view(), name='confirmation-view'),
    path('login/', LoginView.as_view(), name='login-view'),
    path('logout/', LogoutView.as_view(), name='logout-view'),
    path('register/', RegisterView.as_view(), name='register-view'),
    path('profile/<int:pk>/', ProfileView.as_view(), name='profile-view'),
    path('userupdate/<int:pk>/', UserUpdateView.as_view(), name='userupdate-view'),
    path('passwordchange/<int:pk>/', PasswordChangeView.as_view(), name='passwordchange-view'),
    path('get_inst_by_cat/', views.get_inst_by_cat, name='get_inst_by_cat'),
    path('changeview/<int:pk>/', ChangeView.as_view(), name='change-view'),
    # path('taken/<int:pk>/', views.taken_donation, name='taken-view'),
]
