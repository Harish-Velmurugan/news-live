from django.shortcuts import render
from django.views.generic.edit import UpdateView, DeleteView ,CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
# Create your views here.
from django.views.generic import ListView,DetailView
from . import models
class ArticleListView(LoginRequiredMixin,ListView):
    model = models.Article
    login_url = 'login'
    template_name = 'articles/article_list.html'

class ArticleDetailView(LoginRequiredMixin,DetailView):
    model = models.Article
    login_url = 'login'
    template_name = 'articles/article_detail.html'
class ArticleUpdateView(LoginRequiredMixin,UpdateView): 
    model = models.Article
    login_url = 'login'
    fields = ['title', 'body',]
    template_name = 'articles/article_edit.html'
class ArticleDeleteView(LoginRequiredMixin,DeleteView): 
    model = models.Article
    template_name = 'articles/article_delete.html'
    login_url = 'login'
    success_url = reverse_lazy('article_list')


class ArticleCreateView(LoginRequiredMixin,CreateView):
    model = models.Article
    template_name = "articles/article_new.html"
    fields = ['title', 'body',]
    login_url = 'login'
    def form_valid(self,form):
        form.instance.author = self.request.user
        return super().form_valid(form)

