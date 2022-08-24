from django import forms
from .models import Document


class DocumentForm(forms.ModelForm):
    document = forms.FileField()

    class Meta:
        model = Document
        fields = ['document', ]
        document = forms.FileField(
            widget=forms.FileInput(
                attrs={'accept': 'image/*,video/*'}
            ))
