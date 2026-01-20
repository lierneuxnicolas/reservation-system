from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Show


class ShowListView(ListView):
    model = Show
    template_name = "catalog/show_list.html"
    context_object_name = "shows"


class ShowDetailView(DetailView):
    model = Show
    template_name = "catalog/show_detail.html"
    context_object_name = "show"
    slug_field = "slug"
    slug_url_kwarg = "slug"


class ShowCreateView(CreateView):
    model = Show
    fields = ["title", "description", "price", "bookable"]
    template_name = "catalog/show_form.html"
    success_url = reverse_lazy("show_list")


class ShowUpdateView(UpdateView):
    model = Show
    fields = ["title", "description", "price", "bookable"]
    template_name = "catalog/show_form.html"
    slug_field = "slug"
    slug_url_kwarg = "slug"
    success_url = reverse_lazy("show_list")


class ShowDeleteView(DeleteView):
    model = Show
    template_name = "catalog/show_confirm_delete.html"
    slug_field = "slug"
    slug_url_kwarg = "slug"
    success_url = reverse_lazy("show_list")
