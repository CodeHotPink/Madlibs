"""A madlib game that compliments its users."""

from random import choice, sample

from flask import Flask, render_template, request

# "__name__" is a special Python variable for the name of the current module.
# Flask wants to know this to know what any imported things are relative to.
app = Flask(__name__)


COLORS = ["pink","red","white"]
ADJECTIVES = ["big","small","medium"]
ANIMALS = ["dog","cat","hedgehog","yak"]
AWESOMENESS = [
    'awesome', 'terrific', 'fantastic', 'neato', 'fantabulous', 'wowza',
    'oh-so-not-meh', 'brilliant', 'ducky', 'coolio', 'incredible', 'wonderful',
    'smashing', 'lovely',
]
madlib_list = ["madlib.html","madlib2.html", "madlib3.html"]

@app.route('/')
def start_here():
    """Display homepage."""

    return "Hi! This is the home page."


@app.route('/hello')
def say_hello():
    """Say hello to user."""

    return render_template("hello.html")


@app.route('/greet')
def greet_person():
    """Greet user with compliment."""

    player = request.args.get("person")

    compliment = sample(AWESOMENESS, 3)

    return render_template("compliment.html",
                           person=player,
                           compliment= compliment)

@app.route('/game')
def show_madlib_form():
    """show form."""
    response = request.args.get("yesno")
    if response == "no":
        return render_template("goodbye.html")
    if response == "yes":
        return render_template("game.html",
                                colors=COLORS,
                                adjectives=ADJECTIVES,
                                animals=ANIMALS)

@app.route('/madlib', methods=["POST"])
def show_madlib():
    """show madlib"""
    person_name = request.form.get("person_name")
    color = request.form.get("color")
    noun = request.form.get("noun")
    adjective = request.form.get("adjective")
    animals = request.form.getlist("animals")
    animals = ' and '.join(animals)
    madlib = choice(madlib_list)

    return render_template(madlib,
                                person_name=person_name,
                                color=color,
                                noun=noun,
                                adjective=adjective,
                                animals=animals
                                )

if __name__ == '__main__':
    # Setting debug=True gives us error messages in the browser and also
    # "reloads" our web app if we change the code.

    app.run(debug=True)
