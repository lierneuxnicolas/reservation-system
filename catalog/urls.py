from django.urls import path
from . import views

urlpatterns = [
    path("", views.ShowListView.as_view(), name="show_list"),
    path("show/<slug:slug>/", views.ShowDetailView.as_view(), name="show_detail"),
    path("show/add/", views.ShowCreateView.as_view(), name="show_add"),
    path("show/<slug:slug>/edit/", views.ShowUpdateView.as_view(), name="show_edit"),
    path("show/<slug:slug>/delete/", views.ShowDeleteView.as_view(), name="show_delete"),
    path("show/add/", views.ShowCreateView.as_view(), name="show_add"),
    path("artists/", views.artist_index, name="artist_index"),
    path("artists/<int:pk>/", views.artist_show, name="artist_show"),
]
