from django.urls import path

from . import views

app_name = 'fooddash'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'), #/dashboard/
    path('add_recipe', views.AddRecipeView, name='add_recipe'), #/dashboard/add_recipe
    path('<int:pk>/delete/', views.DeleteRecipe.as_view(), name='recipe-delete'),
    path('<int:pk>/edit/', views.EditRecipe.as_view(), name='recipe-edit'),
    # path('<int:pk>/', views.DetailView.as_view(), name='detail'), #/dashboard/5
    # path('<int:pk>/results', views.Resultsview.as_view(), name='results'),
    # path('<int:question_id>/vote/', views.vote, name='vote'),
]
