from django.http import HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, UpdateView, DeleteView
from .models import Post
from .filters import PostFilter
from .forms import PostForm


class News_search(ListView):
    model = Post
    ordering = 'dateCreation'
    template_name = 'news_search.html'
    context_object_name = 'news'

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = PostFilter(self.request.GET, queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filterset'] = self.filterset
        return context


class News(ListView):
    model = Post
    ordering = 'dateCreation'
    template_name = 'news.html'
    context_object_name = 'news'
    paginate_by = 10


class New(DetailView):
    model = Post
    template_name = 'new.html'
    context_object_name = 'new'

@login_required
def CreatePost(request):
    form = PostForm()
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/news/")

    return render(request, 'post_create.html', {"form": form})


class PostUpdate(LoginRequiredMixin, UpdateView):
    raise_exception = True
    form_class = PostForm
    model = Post
    template_name = 'post_edit.html'
    success_url = '/news'


class PostDelete(LoginRequiredMixin, DeleteView):
    raise_exception = True
    model = Post
    template_name = 'post_delete.html'
    success_url = '/news'
