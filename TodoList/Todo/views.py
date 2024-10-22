from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import TodoForm
from .models import Todo

# Create your views here.


class Index(ListView):
    template_name = 'Todo/index.html'
    context_object_name = 'tasks'
    ordering = ['-date']
    model = Todo

    # def get_queryset(self):
    #     return super().get_queryset().filter(author=self.request.user)



class detailViews(DetailView):
    template_name = 'Todo/details.html'
    context_object_name = 'task'
    model = Todo

class createViews(CreateView):
    template_name = 'Todo/create.html'
    form_class = TodoForm
    model = Todo
   

class updateViews(UpdateView):
    template_name = 'Todo/update.html'
    form_class = TodoForm
    model = Todo

class deleteViews(DeleteView):  
    template_name = 'Todo/delete.html'
    success_url = '/tasks'
    model = Todo



    