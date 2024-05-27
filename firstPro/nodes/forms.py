from django.core.exceptions import ValidationError
from django import forms
from .models import notes

class NotesForm(forms.ModelForm):
    class Meta:
        model=notes
        fields=('title','text')
        labels = {'text':'This is my label'}

    # def clean_title(self):
    #     title=self.cleaned_data['title']
    #     if 'django' not in title:
    #         raise ValidationError("We only accept notes about Django")
    #     return title