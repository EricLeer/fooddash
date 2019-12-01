from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse, reverse_lazy
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from django.utils import timezone
from datetime import datetime
from .models import Recipes
from .forms import RecipeForm

from bs4 import BeautifulSoup
import requests
import logging

class IndexView(generic.ListView):
    template_name = 'fooddash/index.html'
    context_object_name = 'recipe_list'

    def get_queryset(self):
        """Return the last five publishd questions(not including future questions)."""
        return Recipes.objects.order_by('-pub_date')[:5]

def AddRecipeView(request):
    if request.method == 'POST':
        form = RecipeForm(request.POST)
        print(form)
        if form.is_valid():
            print(form.cleaned_data)
            data = form.cleaned_data

            ## Get url of image of the recipe
            with requests.get(data['recipe_url']) as r:
                soup = BeautifulSoup(r.content, features="lxml")
                title = soup.title
                img = soup.find(itemprop=["image", "photo"])
                print(img)
                if img:
                    img_url = img["src"]
                    rec = Recipes(
                            recipe_titel=data['recipe_titel'],
                            recipe_url=data['recipe_url'],
                            recipe_img_url=img_url,
                            pub_date=datetime.now(),
                        )
                else:
                    rec = Recipes(
                        recipe_titel=data['recipe_titel'],
                        recipe_url=data['recipe_url'],
                        pub_date=datetime.now(),
                    )
            rec.save()
            ## TODO: add picture url
            return redirect('fooddash:index')
    else:
        form = RecipeForm()

        return render(request, 'fooddash/add_recipe.html', {'form':form})

class DeleteRecipe(DeleteView):
    model = Recipes
    success_url = reverse_lazy('fooddash:index')

    # # TODO correctly implement this logic
    # rec = Recipes.objects.get(id=id)
    # rec.delete()
    # return redirect("fooddash:index")

class EditRecipe(UpdateView):
    model = Recipes
    form_class = RecipeForm
    template_name = "fooddash/add_recipe.html"

    def form_valid(self, form):
      self.object = form.save(commit=False)
      # Any manual settings go here
      self.object.save()
      return redirect('fooddash:index')

    def dispatch(self, request, *args, **kwargs):
        return super(EditRecipe, self).dispatch(request, *args, **kwargs)

    # ## TODO: correctly implement this
    # if request.method == 'POST':
    #     rec = Recipes.object.get(id=id)
    #     form = RecipeForm(instance=rec)

# class DetailView(generic.DetailView):
#     model = Question
#     template_name = 'polls/detail.html'
#
#     def get_queryset(self):
#         """
#         Excludes any questiosn that aren't published yet.
#         """
#         return Question.objects.filter(pub_date__lte=timezone.now())
#
# class Resultsview(generic.DetailView):
#     model = Question
#     template_name = 'polls/results.html'
#
# def vote(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     try:
#         selected_choice = question.choice_set.get(pk=request.POST['choice'])
#     except (KeyError, Choice.DoesNotExist):
#         return render(request, 'polls/detail.html', {
#             'question': question,
#             'error_message': "You didn't select a choice.",
#         })
#     else:
#         selected_choice.votes += 1
#         selected_choice.save()
#         return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
