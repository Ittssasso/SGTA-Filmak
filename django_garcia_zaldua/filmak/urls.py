from django.urls import path

from . import views

app_name = 'filmak'
urlpatterns = [path('', views.index, name='index'),
    path('login/', views.login, name='login'),
    path('signup/', views.signup, name='signup'),
    path('logout/', views.logout, name='logout'),
    path('homefilms/', views.homefilms, name='homefilms'),
    path('filmakikusi/', views.filmakikusi, name='filmakikusi'),
    path('filmakbozkatu/', views.filmakbozkatu, name='filmakbozkatu'),
    path('filmakzaleak/', views.zaleak, name='zaleak'),]
