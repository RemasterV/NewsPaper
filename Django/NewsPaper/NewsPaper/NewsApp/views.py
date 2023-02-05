
from django.views.generic import ListView, DetailView
from .models import Post


class News(ListView):
    model = Post
    ordering = 'dateCreation'
    template_name = 'news.html'
    context_object_name = 'news'

class New(DetailView):
    model = Post
    template_name = 'new.html'
    context_object_name = 'new'