from django.urls import path

from . import views

urlpatterns = [
        path('', views.index, name='index'),
        path('search', views.search, name='search'),
        path('recipe/', views.RecipeListView.as_view(), name="recipe-list"),
        path('recipe_search_results/', views.RecipeSearchResults.as_view(),
            name="recipe-search-results"),
        path('recipe_category_results/<category>/', views.RecipeCategoryResults.as_view(),
            name="recipe-category-results"),
        path('recipe/<int:pk>', views.RecipeDetailView.as_view(), name="recipe-detail"),
        path('categories/', views.CategoryListView.as_view(),
             name="category-list"),
        path('subcategories/', views.SubcategoryListView.as_view(),
             name="subcategories-list"),
]
