from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from .models import notes
from django.http import Http404, HttpResponseRedirect
from  django.views.generic import ListView
from  django.views.generic.detail import  DetailView
from django.views.generic import CreateView
from .forms import NotesForm
from django.views.generic import UpdateView
from django.views.generic.edit import DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView


#from django.core.exceptions import ValidationError

# Create your views here.

# def list(request):
#     all_nodes=notes.objects.all
#     return render(request,'nodes/nodes_list.html',{'nodes':all_nodes})


class listView (ListView,LoginRequiredMixin):

    model = notes
    context_object_name = 'nodes'
    template_name='nodes/nodes_list.html'

    login_url='/admin'
    def get_queryset(self):
        return self.request.user.notes.all()
    

class detailView (DetailView,LoginRequiredMixin):
  model = notes
  context_object_name = 'node'
  template_name = 'nodes/detail.html'
  login_url='/admin'

def detail(request,pk):
    try:
        node = notes.objects.get(pk=pk)
        return render(request,'nodes/detail.html',{'node':node})
    except notes.DoesNotExist:  
        raise Http404('Notes does not exist')
    
class createView(LoginRequiredMixin,CreateView):
    template_name="nodes/notes_form.html"
    model=notes
    success_url="/smart/nodes"
    form_class=NotesForm
    login_url='/admin'

    def form_valid(self,form):
        self.object=form.save(commit=False)
        self.object.user=self.request.user
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())

# class class_title():
#         title = self.clean_data['title']

# def clean_data(self):
#          title=self.clean_data['title']
#             if 'django' not in title:
#                                     raise ValidationError('we need django')
#                                    reutrn title
class UpdateView(LoginRequiredMixin,UpdateView):
    model = notes
    success_url = '/smart/nodes'
    form_class = NotesForm
    login_url='/admin'

class DeleteView(LoginRequiredMixin,DeleteView):
    model=notes
    success_url= '/smart/nodes'
    template_name= 'nodes/notes_confirm_delete.html'
    login_url='/admin'
