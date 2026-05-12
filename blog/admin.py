from django.contrib import admin
from .models import Article,Commentaire,Categorie


class CategorieAdmin(admin.ModelAdmin):
    list_display = ('nom_categorie', 'description')
    search_fields = ('nom_categorie', 'description', 'date_creation')
    list_filter = ('nom_categorie', 'date_creation')


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('titre', 'date_publication', 'auteur', 'publier')
    search_fields = ('titre', 'contenu', 'categorie', 'auteur')
    list_filter = ('publier', 'date_publication')


class CommentaireAdmin(admin.ModelAdmin):
    list_display = ('message', 'article', 'username')
    search_fields = ('message', 'article', 'username', 'date_commentaire')
    list_filter = ('username', 'article', 'date_commentaire')

admin.site.register(Article, ArticleAdmin)
admin.site.register(Commentaire, CommentaireAdmin)
admin.site.register(Categorie, CategorieAdmin)

