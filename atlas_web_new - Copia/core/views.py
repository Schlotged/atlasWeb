from django.shortcuts import render
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import CreateView
from django.contrib.auth import login
from django.urls import reverse_lazy
from django.shortcuts import redirect
from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required



class CustomLoginView(LoginView):
    
    template_name = 'partials/_login.html'
    redirect_authenticated_user = True
    success_url = reverse_lazy('task:home')

    def get_success_url(self):
        return self.success_url


class CustomRegisterView(CreateView):
    form_class = UserCreationForm
    template_name = 'partials/_register.html'
    success_url = reverse_lazy('task:home')

    def form_valid(self, form):

        response = super().form_valid(form)

        user = form.save()
        login(self.request, user)
        
        return response

    def get_success_url(self):

        return self.success_url

    def get(self, request, *args, **kwargs):

        if request.user.is_authenticated:
            return redirect(self.success_url)
        return super().get(request, *args, **kwargs)
    
def logout_view(request):
    auth.logout(request)
    return redirect('login')