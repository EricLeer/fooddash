from django import forms
from .models import Recipes
# class RecipeForm(forms.Form):
#     recipe_titel = forms.CharField(max_length=200)
#     recipe_url = forms.URLField()

class RecipeForm(forms.ModelForm):
    recipe_titel = forms.CharField(max_length=200)
    recipe_url = forms.URLField()
    class Meta:
        model = Recipes
        fields = ['recipe_titel', 'recipe_url']

# class PostForm(forms.ModelForm):
#     title = forms.CharField(max_length=128, help_text="plz enter")
#     views = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
#     class Meta:
#         model = Post
#         fields = ['title', 'content', 'image', 'views', 'category']
