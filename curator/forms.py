from django import forms
from .models import *


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = '__all__'

        #widgets = {
          #  'title' = forms.TextInput(attrs={'class': 'form-control'}),
          #  'author' = forms.TextInput(attrs={'class': 'form-control'}),

       # }


class MovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = '__all__'


class AlbumForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = '__all__'