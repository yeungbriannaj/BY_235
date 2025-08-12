from typing import List, Dict
from datetime import date
from .category import Category
from errors.CategorisationError import CategorisationError

class Recipe:
    def __init__(self,
                 recipe_id: int,
                 name: str,
                 author: str,
                 instructions: str,
                 images: List[str] = None,
                 ingredients: List[str] = None,
                 ingredient_quantities: Dict[str, str] = None,
                 date_added: date = None,
                 rating: float = 0.0,
                 preparation_time: int = 0,
                 cook_time: int = 0,
                 recipe_yield: str = "",
                 servings: int = 0,
                 description: str = "",
                 reviews: List[str] = None,
                 categories: List['Category'] = None):

        self.__recipe_id = recipe_id
        self._name = name
        self._author = author
        self._instructions = instructions
        self._description = description
        
        # Using default values if not provided
        self._images = images or []
        self._ingredients = ingredients or []
        self._ingredient_quantities = ingredient_quantities or {}
        self._date_added = date_added or date.today()
        self._rating = rating
        self._preparation_time = preparation_time
        self._cook_time = cook_time
        self._recipe_yield = recipe_yield
        self._servings = servings
        self._reviews = reviews or []
        self._categories: List[Category] = []

        # Loops through any initial categories provided and uses the safe method to add them
        if categories:
            for category in categories:
                self.add_to_category(category)

    @property
    def id(self) -> int:
        return self.__recipe_id

    @property
    def name(self) -> str:
        return self._name
    
    @property
    def author(self) -> str:
        return self._author

    @name.setter
    def name(self, value: str):
        if not value or not value.strip():
            raise ValueError("Recipe name cannot be empty.")
        self._name = value

    @property
    def categories(self) -> List['Category']:
        return list(self._categories)

    def add_to_category(self, new_category: 'Category'):
        if new_category in self._categories:
            raise CategorisationError(f"Recipe is already in category '{new_category.name}'.")        
        new_category.add_recipe(self)
        self._categories.append(new_category)

    def remove_from_category(self, category: 'Category'):
        if category not in self._categories:
            raise CategorisationError(f"Recipe is not in category '{category.name}'.")
        
        if len(self._categories) <= 1:
            raise CategorisationError("Recipe must belong to at least one category.")

        category.remove_recipe(self)
        self._categories.remove(category)

    def __eq__(self, other):
        if not isinstance(other, Recipe):
            return NotImplemented
        return self.__recipe_id == other.__recipe_id

    def __hash__(self):
        return hash(self.__recipe_id)

    def __str__(self):
        category_names = ", ".join(c.name for c in self._categories)
        return f"'{self._name}' by {self._author} | Categories: [{category_names}]"
    
    def __repr__(self):
        return f"<Recipe id={self.__recipe_id} name='{self._name}'>"