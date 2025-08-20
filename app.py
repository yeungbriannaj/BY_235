from flask import Flask, render_template, abort

app = Flask(__name__,
            template_folder='Recipes/templates',
            static_folder='Recipes/static')

# DUMMY DATA
recipes_data = [
    {
        "id": 1,
        "title": "Fluffy Pancakes",
        "image": "images/pancakes.jpg",
        "description": "Classic, easy-to-make pancakes for a perfect breakfast.",
        "ingredients": [
            "2 cups plain flour",
            "4 tsp baking powder",
            "1/4 cup white sugar",
            "1 egg",
            "1 3/4 cups milk"
        ],
        "instructions": [
            "Place flour, baking powder, sugar and salt in a bowl, whisk to combine.",
            "Add egg, milk and vanilla. Whisk until lump free.",
            "Heat a lightly oiled griddle or frying pan over medium high heat.",
            "Pour or scoop the batter onto the griddle.",
            "Brown on both sides and serve hot."
        ]
    },
    {
        "id": 2,
        "title": "Classic Lemonade",
        "image": "images/lemonade.jpg",
        "description": "A refreshing and simple homemade lemonade.",
        "ingredients": [
            "1 cup white sugar",
            "1 cup water (for syrup)",
            "1 cup lemon juice",
            "3 to 4 cups cold water (to dilute)"
        ],
        "instructions": [
            "Make simple syrup by heating sugar and 1 cup of water in a small saucepan until the sugar is dissolved completely.",
            "While syrup is cooling, juice your lemons.",
            "Pour the juice and syrup into a pitcher.",
            "Add 3 to 4 cups of cold water, depending on how concentrated you like your lemonade.",
            "Stir and chill before serving."
        ]
    },
    {
        "id": 3,
        "title": "Simple Pasta",
        "image": "images/pasta.jpg",
        "description": "A quick and delicious pasta dish.",
        "ingredients": [
            "500g pasta",
            "1 jar of your favorite pasta sauce",
            "Parmesan cheese, for serving",
            "Fresh basil, for garnish"
        ],
        "instructions": [
            "Cook pasta according to package directions.",
            "While pasta is cooking, heat the pasta sauce in a saucepan.",
            "Drain the pasta and add it to the sauce.",
            "Toss to combine and serve with a sprinkle of Parmesan and fresh basil."
        ]
    }
]


@app.route('/')
@app.route('/home')
def index():
    return render_template('index.html')

@app.route('/recipe/<int:recipe_id>')
def recipe_detail(recipe_id):
    recipe = next((r for r in recipes_data if r['id'] == recipe_id), None)
    if recipe is None:
        abort(404)
    return render_template('recipe_detail.html', recipe=recipe)

@app.route('/browse')
def browse():
    return render_template('browse.html', recipes=recipes_data)

@app.route('/category')
def category():
    return render_template('category.html')

@app.route('/about')
def about():
    return "<h1>About</p>"

if __name__ == '__main__':
    app.run(debug=True)