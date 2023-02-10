from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib import messages
from django.views import generic, View
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Wine
from .forms import WineForm

class WineList(LoginRequiredMixin, ListView):
    model = Wine
    template_name = 'wines.html'


class WineDetailView(DetailView):
    model = Wine
    template_name = 'wine_details.html'

class WineCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Wine
    template_name = 'add_wine.html'
    form_class = WineForm
    success_message = 'Wine was added successfully'
    success_url = reverse_lazy('wines')

    def form_valid(self, form):
        form.instance.posted_by = self.request.user
        return super().form_valid(form)





# def add_wine(request):
#     form = WineForm()
#     if request.method == 'POST':
#         form = WineForm(request.POST, request.FILES)
#         if form.is_valid():
#             event = form.save(commit=False)
#             event.posted_by = request.user
#             event.save()
#             messages.success(request, 'Your recipe was added successfully')
#             return redirect('wines')
    
#     context = {'form': form}
#     return render(request, 'add_wine.html', context)


