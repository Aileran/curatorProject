from django import forms
from .models import *


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = '__all__'


class MovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = '__all__'


class AlbumForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = '__all__'