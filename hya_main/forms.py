from django import forms
from django.views.generic.edit import UpdateView, DeleteView
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, User
from .models import Clanek, Postava, Page
from django.forms import DateTimeInput


class ClanekForm(forms.ModelForm):
    class Meta:
        model = Clanek
        fields = ('titulek', 'postava', 'kategorie', 'obsah', 'obrazek',)


class RegistraceForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username',)


class PrihlaseniForm(AuthenticationForm):
    class Meta:
        model = User


class PostavaForm(forms.ModelForm):
    class Meta:
        model = Postava
        fields = ('jmeno', 'prijmeni', 'narozeni', 'narodnost', 'vyska', 'nabozenstvi',
                  'politika', 'vzdelani', 'rodice', 'jazyky', 'hobby', 'bio',)


class PageForm(forms.ModelForm):
    class Meta:
        model = Page
        fields = ('title', 'tags', 'content',)


class PageUpdateForm(UpdateView):
    class Meta:
        model = Page
        fields = ('title', 'tags', 'content')


class PageDeleteForm(UpdateView):
    class Meta:
        model = Page


# class DeleteThing(DeleteView):
#    model = Clanek
#    success_url = reverse_lazy('author-list')
