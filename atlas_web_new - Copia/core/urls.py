
from django.contrib import admin
from django.urls import path, include
from .views import CustomLoginView, CustomRegisterView, logout_view

app_name = 'core'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('task.urls')),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('register/', CustomRegisterView.as_view(), name='register'),
    path('logout/', logout_view, name='logout'),
    
    
]
