from django.contrib import admin

# Register your models here.
from .models import Recipe, Category, Subcategory, Ingredient

class RecipeAdmin(admin.ModelAdmin):
    list_display = ('title',)
    filter_horizontal = ('ingredients','subcategories',)
    # search_fields = ('title',)
    #list_filter = ('category', 'language',)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)


class SubcategoryAdmin(admin.ModelAdmin):
    list_display = ('name','category')


class IngredientAdmin(admin.ModelAdmin):
    list_display = ('name',)

admin.site.register(Recipe, RecipeAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Subcategory, SubcategoryAdmin)
admin.site.register(Ingredient, IngredientAdmin)
