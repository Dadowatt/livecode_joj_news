from django.shortcuts import render
from .models import Article, Categorie, Commentaire
from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView
from .forms import CommentaireForm
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
class ArticleListView(ListView):
    model = Article
    template_name = 'liste_article.html'
    context_object_name = 'articles'


class CategorieListView(ListView):
    model = Categorie
    template_name = 'liste_categorie.html'
    context_object_name = 'categories'

class ArticleDetailView(DetailView):
    model = Article
    template_name = 'detail_article.html'
    context_object_name = 'article'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['form'] = CommentaireForm()
        return context 
    

class AjouterCommentaireView(LoginRequiredMixin, CreateView):
    model = Commentaire
    form_class = CommentaireForm

    def form_valid(self, form):

        article = Article.objects.get(pk=self.kwargs['pk'])

        form.instance.article = article
        form.instance.username = self.request.user

        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy(
            'detail_article',
            kwargs={'pk': self.kwargs['pk']}
        )


class ModifierCommentaireView(LoginRequiredMixin, UpdateView):
    model = Commentaire
    form_class = CommentaireForm
    template_name = 'modifier_commentaire.html'

    def get_success_url(self):
        return reverse_lazy(
            'detail_article',
            kwargs={'pk': self.object.article.pk}
        )


class SupprimerCommentaireView(LoginRequiredMixin, DeleteView):
    model = Commentaire
    template_name = 'supprimer_commentaire.html'

    def get_success_url(self):
        return reverse_lazy(
            'detail_article',
            kwargs={'pk': self.object.article.pk}
        )