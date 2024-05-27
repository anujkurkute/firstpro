from django.shortcuts import render

from django.http import HttpResponse
from datetime import datetime

from django.contrib.auth.decorators import login_required
from  django.views.generic import TemplateView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView,LogoutView
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect

# Create your views here.

# def home(request):
#     # return HttpResponse('Hello World')
#     return render(request,'Home/welcome.html',{'today':datetime.today()})

# @login_required(login_url='/admin')
# def authorize(request):
#     return render(request,'Home/authorize.html',{})

class HomeView(TemplateView):
        template_name =  'Home\welcome.html'
        extra_context = {'today':datetime.today()}  

class AuthorizedView(LoginRequiredMixin,TemplateView):
    template_name = 'Home/authorize.html'
    login_url = '/admin'
      
class LoginInterfaceView (LoginView):
      template_name =  'Home/login.html'
     
class LogoutInterfaceView(LogoutView):
      template_name='Home/logout.html'

class SignupView(CreateView):
      form_class= UserCreationForm 
      template_name = 'Home/register.html'
      success_url = 'smart/nodes'
      def get(self, request, *args, **kwargs):
            if self.request.user.is_authenticated:
                    # return redirect('smart:nodes')
                    return redirect('nodes.list')
            return super().get(request, *args, **kwargs)