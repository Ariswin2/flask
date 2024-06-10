# import the required packages
from flask import Flask
import random


# store a number between 0 to 9 using random package with randint method
random_number = random.randint(0,9)
print(random_number)

app = Flask(__name__)
# first create main page which is for guess the value
# In search bar after the server path put backslash(/) and what you guess a number between 0 to 9
@app.route("/")
def home():
    return '<h1>Guess a Number Between 0 to 9 </h1>'\
            "<img src='https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif'/>"


@app.route("/<int:guess>")
def guess_number(guess):
    # This is for, if the random_number greater than
    # you typed number is  "It's too high" and display some gif image
    if guess > random_number:
        return "<h1 style='color: red'>Too High, Try Again!</h1>"\
                "<img src='https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif'/>"
    # This part will so if the random_number is lesser
    # than you typed number then it's shown "It's Too Low" and display some gif image
    elif guess < random_number:
        return "<h1 style='color: purple'>Too Low, Try Again!</h1>"\
                "<img src='https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif'/>"
    # and this code will do you typed number was equal
    # to random_number then its shown "YOU FOUND IT" and display one gof image
    else:
        return "<h1 style='color: green'>YOU FOUND ME!</h1>"\
                "<img src='https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif'/>"


if __name__ == "__main__":
    app.run(debug=True)


