from django.urls import path 
from .views import ArticleListView, CategorieListView, ArticleDetailView,AjouterCommentaireView,ModifierCommentaireView,SupprimerCommentaireView


urlpatterns = [
    path('articles', ArticleListView.as_view(), name='liste_article'),
    path('categories', CategorieListView.as_view(), name='liste_categorie'),
    path('detail_article/<int:pk>', ArticleDetailView.as_view(), name='detail_article'),
    path('ajouter_commentaire/<int:pk>/',AjouterCommentaireView.as_view(),name='ajouter_commentaire'),
    path('modifier_commentaire/<int:pk>/',ModifierCommentaireView.as_view(),
    name='modifier_commentaire'
    ),
    path('supprimer_commentaire/<int:pk>/',SupprimerCommentaireView.as_view(),
    name='supprimer_commentaire'
    ),
]

