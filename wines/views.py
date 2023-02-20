from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib import messages
from django.views import generic, View
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Wine
from .forms import WineForm

class WineList(LoginRequiredMixin, ListView):
    """
    Displays all the Wines
    """
    model = Wine
    paginate_by = 6
    template_name = 'wines.html'


class WineDetailView(LoginRequiredMixin, DetailView):
    """
    This provides the detailed view of the wine
    """
    model = Wine
    template_name = 'wine_details.html'

class WineCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    """
    View to Add a wine
    """
    model = Wine
    template_name = 'add_wine.html'
    form_class = WineForm
    success_message = 'Wine was added successfully'
    success_url = reverse_lazy('wines')

    def form_valid(self, form):
        form.instance.posted_by = self.request.user
        return super().form_valid(form)


class WineUpdateView(LoginRequiredMixin, UpdateView):
    """ 
    View to edit a wine
    """
    model = Wine
    template_name = 'edit_wine.html'
    form_class = WineForm


class WineDeleteView(LoginRequiredMixin, DeleteView):
    """ 
    View to edit a wine
    """
    model = Wine
    success_url = reverse_lazy('wines')
    template_name = 'wines.html'