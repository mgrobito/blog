from django.urls import path
from .views import BlogList

urlpatterns = [
    path('', BlogList, name="blog_list"),
]
