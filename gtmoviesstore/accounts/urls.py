from django.urls import path
from . import views
<<<<<<< HEAD

urlpatterns = [
    path('signup', views.signup, name='accounts.signup'),
=======
urlpatterns = [
    path('signup', views.signup, name='accounts.signup'),
    path('login/', views.login, name='accounts.login'),
    path('logout/', views.logout, name='accounts.logout'),
>>>>>>> 81323c8307e9938b336bdafd15e7d71f830a5bfd
]