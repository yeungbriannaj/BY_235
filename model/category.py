from errors.CategorisationError import CategorisationError

class Category:
    def __init__(self, category_id: int, name: str):
        self.__category_id = category_id
        self._name = name
        self.__recipes: list["Recipe"] = []

    @property
    def id(self) -> int:
        return self.__category_id

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, value: str):
        if not value or not value.strip():
            raise ValueError("Category name cannot be empty.")
        self._name = value
        
    @property
    def recipe_count(self) -> int:
        return len(self.__recipes)

    def add_recipe(self, recipe: "Recipe"):
        if recipe in self.__recipes:
            raise CategorisationError(f"Recipe '{recipe.name}' is already in category '{self.name}'.")
        self.__recipes.append(recipe)

    def remove_recipe(self, recipe: "Recipe"):
        if recipe not in self.__recipes:
            raise CategorisationError(f"Recipe '{recipe.name}' is not in category '{self.name}'.")
        self.__recipes.remove(recipe)

    def __eq__(self, other):
        if not isinstance(other, Category):
            return NotImplemented
        return self.__category_id == other.__category_id

    def __hash__(self):
        return hash(self.__category_id)

    def __str__(self):
        return f"{self.name} ({self.recipe_count} recipes)"

    def __repr__(self):
        return f"<Category id={self.__category_id} name='{self._name}'>"