from django.shortcuts import render, redirect
from django.contrib import messages
from django.views import generic, View
from django.views.generic import ListView, CreateView
from .models import Wine
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from .forms import WineForm

class WineList(LoginRequiredMixin, ListView):
    model = Wine
    template_name = 'wines.html'

@login_required
def add_wine(request):
    form = WineForm()
    if request.method == 'POST':
        form = WineForm(request.POST, request.FILES)
        if form.is_valid():
            event = form.save(commit=False)
            event.posted_by = request.user
            event.save()
            messages.success(request, 'Your recipe was added successfully')
            return redirect('wines')
    
    context = {'form': form}
    return render(request, 'add_wine.html', context)