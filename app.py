# FILE: app.py
from flask import Flask, render_template

app = Flask(__name__,
            template_folder='Recipes/templates',
            static_folder='Recipes/static')

# The function name 'index' MATCHES url_for('index')
@app.route('/')
def index():
    return render_template('index.html')

# The function name 'browse' MATCHES url_for('browse')
@app.route('/browse')
def browse():
    return render_template('browse.html')

# The function name 'category' MATCHES url_for('category')
@app.route('/category')
def category():
    return render_template('category.html')

# This is a placeholder for your about page
@app.route('/about')
def about():
    # You'll need to create an about.html template as well
    return "<h1>About Page Coming Soon!</h1>"

# The function name 'recipe_detail' MATCHES url_for('recipe_detail')
@app.route('/recipe')
def recipe_detail():
    # Eventually this will be dynamic, like /recipe/1 for pancakes
    return render_template('recipe_detail.html')

# This part is important for running the app
if __name__ == '__main__':
    app.run(debug=True)