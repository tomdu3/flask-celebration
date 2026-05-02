from flask import Flask, render_template
import requests

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
    my_friends=['fajar','neethu','Tomi','Rohini']

    return render_template("index.html", context=context, Heading=Heading,
                           My_stuff=My_stuff,my_friends=my_friends)

@app.route("/guess/<name>")
def guess(name):
    gender_url=f"https://api.genderize.io?name={name}"
    age_url=f"https://api.agify.io?name={name}"
    get_age_url_response=requests.get(age_url)
    get_age_url_data=get_age_url_response.json()
    age=get_age_url_data["age"]
    get_gender_response=requests.get(gender_url)
    get_gender_data=get_gender_response.json()
    gender=get_gender_data["gender"]
    
    return render_template("guess.html",gues_name=name,gender=gender,age=age)
    

if __name__ == "__main__":
    app.run(debug=True)
