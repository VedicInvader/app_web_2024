from django.urls import path
from . import views
from django.contrib import admin

urlpatterns = [
    path('admin/', admin.site.urls),
    path('inicio/',views.index, name='inicio'),
    path('',views.index, name='inicio'),
    path('acercade/',views.about, name='acercade'),
    path('mision/',views.mision, name='mision'),
    path('vision/',views.vision, name='vision'),
    path('registro/',views.register_user, name='registro'),
    path('login/',views.login_user, name='login_user'),
    path('logout/', views.logout_user, name='logout_user'),
]