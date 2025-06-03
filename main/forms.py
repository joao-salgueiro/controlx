from django import forms

from main.models import GamingController

class GamingControllerForm(forms.ModelForm):
    class Meta:
        model = GamingController
        fields = ['title', 'description', 'image']
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Digite o título'}),
            'description': forms.Textarea(attrs={'placeholder': 'Escreva a descrição', 'rows': 4}),
            'image': forms.FileInput(),
        }