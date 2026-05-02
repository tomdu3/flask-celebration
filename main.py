from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def home():
    context = {
        "title": "Hello, Sumi!",
        "message": "This is a test.",
        "name": "Sumi",
        "age": 25,
        "is_student": True,
        "hobbies": ["reading", "coding", "playing games"],
        "friends": ["Tom", "Jerry", "Harry"],
    }
    Heading = "Welcome to Flask!"
    My_stuff="Flask is fun!"

    return render_template("index.html", context=context, Heading=Heading,
                           My_stuff=My_stuff)


if __name__ == "__main__":
    app.run(debug=True)
