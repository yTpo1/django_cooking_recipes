from django.db import models


class Ingredient(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=200)

    # in admin in dropdown will display with a name
    def __str__(self):
        return self.name


class Subcategory(models.Model):
    name = models.CharField(max_length=200)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Recipe(models.Model):
    title = models.CharField(max_length=200)
    # method
    ingredients_text = models.TextField()
    instructions = models.TextField()
    image = models.ImageField(default="default.jpg", upload_to="recipe_images")
    difficulty = models.CharField(max_length=200)
    prep_time = models.IntegerField()
    cook_time = models.IntegerField()
    total_time = models.IntegerField()
    ingredients = models.ManyToManyField(Ingredient)
    subcategories = models.ManyToManyField(Subcategory)
    motivation_text = models.TextField(null=True, blank=True, default="")

    def __str__(self):
        return self.title


#class IngredientsInRecipe(models.Model):
#    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
#    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
#    quantity = models.IntegerField(default=1)


