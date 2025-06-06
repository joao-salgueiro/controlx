from django import forms

from main.models import GamingController

class GamingControllerForm(forms.ModelForm):
    class Meta:
        model = GamingController
        fields = ['title', 'description', 'image']
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Title'}),
            'description': forms.Textarea(attrs={'placeholder': 'Description', 'rows': 4}),
            'image': forms.FileInput(),
        }

        def clean_description(self):
            desc = self.cleaned_data.get('description')
            if len(desc) > 300:
                raise forms.ValidationError("Max 300.")
            return desc