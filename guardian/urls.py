from django.urls import path
from guardian import views

urlpatterns = [
    path('login/', views.loginpage, name='LoginPage'),
    path('logout/', views.logoutpage, name='LogoutPage'),
    path('register/', views.registerpage, name='RegisterPage')
]
