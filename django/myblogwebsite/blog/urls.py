from django.urls import path
from . import views

urlpatterns = [
    path("", views.post_list, name="post_list"),
    path("post/<int:post_id>/", views.post_detail, name="post_detail"),
    path("search/", views.post_search, name="post_search"),
    path("contact/", views.contact, name="contact"),
    path("post/create/", views.post_create, name="post_create"),
]
