from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import Recipe, Ingredient, Category, Subcategory

from django.http import HttpResponseRedirect
from .forms import NavSearchForm

class RecipeDetailView(generic.DetailView):
    model = Recipe
    template_name = 'recipes/recipe_detail.html'

    def get_context_data(self, **kwargs):
        context = super(RecipeDetailView, self).get_context_data(**kwargs)
        instructions = context["recipe"].instructions
        ingredients = context["recipe"].ingredients_text
        context.update({
            "instructions_par": instructions.splitlines(),
            "ingredient_list": ingredients.splitlines(),
            #"more_context": Model.objects.all()
        })
        return context


class RecipeListView(generic.ListView):
    model = Recipe
    template_name = 'recipes/recipe_list.html'
    context_object_name = "recipes"


class RecipeCategoryResults(generic.ListView):
    #model = Recipe
    template_name = 'recipes/recipe_search_results.html'
    context_object_name = "recipes"

    def get_queryset(self):
        category = get_object_or_404(Subcategory, name=self.kwargs['category'])
        #return Recipe.objects.filter(subcategories__icontains=category)
        return Recipe.objects.filter(subcategories__exact=category)


class RecipeSearchResults(generic.ListView):
    model = Recipe
    template_name = 'recipes/recipe_search_results.html'
    context_object_name = "recipes"

    def get_queryset(self):
        query = self.request.GET.get('q')
        return Recipe.objects.filter(title__icontains=query)


class SubcategoryListView(generic.ListView):
    model = Subcategory
    template_name = 'recipes/subcategory_list.html'
    context_object_name = "subcategories"


class CategoryListView(generic.ListView):
    model = Category
    template_name = 'recipes/category_list.html'
    context_object_name = "categories"

    def get_context_data(self, **kwargs):
        context = super(CategoryListView, self).get_context_data(**kwargs)
        context.update({
            "subcategories": Subcategory.objects.order_by('name'),
            #"more_context": Model.objects.all()
        })
        return context


def search(request):
    if request.method == 'POST':
        form = NavSearchForm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect('/thanks/')
    else:
        form = NavSearchForm()

    return render(request, 'recipes/search_form.html', {'form': form})


def index(request):
    return render(request, "recipes/index.html")
    #return render(request, "recipes/index_gif.html")
    #return render(request, "recipes/index_gif2.html")
