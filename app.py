# import the Flask class from the flask module
from flask import Flask, render_template, request
import main
# create the application object
app = Flask(__name__)


# use decorators to link the function to a url
@app.route('/')
def home():
    return render_template('downloadmusic.html')
    if request.method == 'POST' | request.method == 'GET':
        if request.form['submit'] == 'GetMyMusic':
            main.download()

# start the server with the 'run()' method
if __name__ == '__main__':
    app.run(debug=True)
