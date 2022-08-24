from django import forms
from .models import Document


class DocumentForm(forms.ModelForm):
    document = forms.FileField()
    description = forms.Textarea()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['document'].label = 'Upload Your File'
        self.fields['document'].required = True
        self.fields['document'].widget.attrs.update({'class': 'form-control', 'type': 'file'})
        self.fields['description'].label = 'File description'
        # self.fields['description'].placeholder = 'Add some description to your file you will upload....'

    class Meta:
        model = Document
        fields = ['document', 'description', ]
