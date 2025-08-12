from model.recipe import Recipe
from datetime import date
from model.category import Category
from errors.CategorisationError import CategorisationError

if __name__ == "__main__":
    cat_dessert = Category(1, "Desserts")
    cat_vegan = Category(2, "Vegan")

    recipe1 = Recipe(
        recipe_id=101,
        name="Chocolate Cake",
        images=["choc_cake1.jpg", "choc_cake2.jpg"],
        ingredients=["Flour", "Sugar", "Cocoa Powder", "Eggs"],
        ingredient_quantities={"Flour": "2 cups", "Sugar": "1.5 cups", "Cocoa Powder": "0.75 cup", "Eggs": "3"},
        author="Alice",
        date_added=date(2025, 8, 3),
        rating=4.5,
        preparation_time=20,
        cook_time=30,
        instructions="Mix ingredients and bake at 350F for 30 minutes.",
        categories=[cat_dessert],
        recipe_yield="1 cake",
        servings=8,
        description="A rich chocolate cake perfect for celebrations.",
        reviews=["Delicious!", "My family loved it."]
    )

    recipe2 = Recipe(
        recipe_id=102,
        name="Vegan Salad",
        images=["vegan_salad.jpg"],
        ingredients=["Lettuce", "Tomatoes", "Cucumber", "Olive Oil"],
        ingredient_quantities={"Lettuce": "1 head", "Tomatoes": "2", "Cucumber": "1", "Olive Oil": "2 tbsp"},
        author="Bob",
        date_added=date(2025, 8, 3),
        rating=4.0,
        preparation_time=10,
        cook_time=0,
        instructions="Chop all ingredients and toss with olive oil.",
        categories=[cat_vegan],
        recipe_yield="1 bowl",
        servings=2,
        description="Fresh and healthy vegan salad.",
        reviews=["Very refreshing!", "Easy to make."]
    )

    print(recipe1)
    print(recipe2)

    cat_dessert.add_recipe(recipe1)
    cat_vegan.add_recipe(recipe2)

    print(cat_dessert)
    print("Recipes in Dessert category:", cat_dessert.recipes)

    print(cat_vegan)
    print("Recipes in Vegan category:", cat_vegan.recipes)