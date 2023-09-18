from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView
from .models import Task
from django.contrib.auth.mixins import LoginRequiredMixin





# Create your views here.
class taskCreatView(LoginRequiredMixin,CreateView):
    model = Task
    fields = ['title','description','completed']
    #success_url = reverse_lazy('tasks-list')

    # This method is called when valid form data has been POSTed.
    # It should return an HttpResponse.
    def form_valid(self, form):
        print(self.request.user)
        form.instance.created_by = self.request.user
        return super().form_valid(form)
    def get_success_url(self):
        return reverse_lazy('tasks-list')
class taskListView(LoginRequiredMixin,ListView):
    model = Task
