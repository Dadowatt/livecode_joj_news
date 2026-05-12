from django import forms 
from .models import Commentaire

from django import forms
from .models import Commentaire

class CommentaireForm(forms.ModelForm):

    class Meta:
        model = Commentaire
        fields = ['message']

        widgets = {
            'message': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Ajouter un commentaire...',
                'rows': 4
            })
        }