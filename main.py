from model.recipe import Recipe
from datetime import date
from model.category import Category
from errors.CategorisationError import CategorisationError

if __name__ == "__main__":
    drinks = Category(1, "Drinks")
    desserts = Category(2, "Desserts")

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
        categories=[],
        recipe_yield="1 cake",
        servings=8,
        description="A rich chocolate cake perfect for celebrations.",
        reviews=["Delicious!", "My family loved it."]
    )

    recipe2 = Recipe(
        recipe_id=102,
        name="Lemonade",
        images=["lemonade.jpg"],
        ingredients=["Lemon", "Sugar", "Water"],
        ingredient_quantities={"Lemon": "1", "Sugar": "50g", "Water": "1 cup"},
        author="Monkey D. Luffy",
        date_added=date(2025, 8, 3),
        rating=4.0,
        preparation_time=10,
        cook_time=0,
        instructions="Squeeze lemonade into a cup, add sugar and water and stir.",
        categories=[],
        recipe_yield="1 bowl",
        servings=2,
        description="Fresh Lemonade.",
        reviews=["Very refreshing!", "Easy to make."]
    )

    print(recipe1)
    print(recipe2)

    recipe1.add_to_category(desserts)
    recipe2.add_to_category(drinks)
    print(f"Category {desserts}")
    print(f"Category {drinks}")
  