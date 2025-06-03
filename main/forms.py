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

        def clean_description(self):
            desc = self.cleaned_data.get('description')
            if len(desc) > 300:
                raise forms.ValidationError("A descrição não pode ter mais de 300 caracteres.")
            return desc