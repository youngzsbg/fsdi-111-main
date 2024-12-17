from flask import Flask   # from the flask module import the Flask class
#OOP = object oriented paradigm
app = Flask(__name__) #When you create an instance of a class, you get an object; app is now an object

@app.route("/")
def hello():
    return "<h1>Hello, world</h1>"

@app.get("/aboutme")     #Flask decorator that allows us to define routes
def home():
    me = {          # python3 dictionary
        "first_name": "Kendall",
        "last_name": "Payne",
        "hobbies": "Ping Pong, Gaming",
        
    }

    return me         #When you return a dictionary from a flask view function, it's converted to JSON