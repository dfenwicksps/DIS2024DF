from flask import Flask  # First we imported the Flask class.

app = Flask(__name__)  # Next we create an instance of this class.

@app.route('/')  # We then use the route() decorator to tell
                # Flask what URL should trigger our function.
def hello_form():
    return "<h3>Hello, this is a form!</h3>"
    # The function returns the message we want to display
    # in the user’s browser.

#if __name__ == '__main__':
#    app.run(debug=True)
