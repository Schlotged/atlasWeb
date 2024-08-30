
from django.urls import path
from task import views

app_name = 'task'

urlpatterns = [
    path('home/', views.index, name='home'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('agendamento/', views.agendamento, name='agendamento'),
    path('senior/', views.form_db, name='senior'),
    path('prestador/', views.form_prestador, name='prestador'),
    path('buscar-prestador/', views.buscar_prestador, name='buscar-prestador'),
    path('buscar-cliente/', views.buscar_cliente, name='buscar-cliente'),
    path('send-senior-odc/', views.send_request_senior_odc, name='senior-ordem-compra'),
    path('send-soc-senior/', views.send_request_senior_soc_prestador, name='soc-senior-prestador'),
    path('buscar-cep/', views.buscar_cep, name='buscar_cep'),
    path('buscar-user/', views.buscar_user, name='buscar_user_soc'),
]
