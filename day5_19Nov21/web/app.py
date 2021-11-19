### Pre-requisite - HTML 5 (DOM) - CSS3 

from flask import Flask

app = Flask(__name__)  # Internally contains http server (localhost:5000)
                        # Tell flask to check fo functions in __name__ thread = __main__

@app.route('/')
@app.route('/home')
def home(): ## Callable from the browser
    # write db, api call, csv, json
    return "<h1>Welcome to BofA</h1>"

@app.route('/about')
def about():
    return "<h2>about BofA - since 1875 </h2>"

if __name__ == '__main__':
    app.run(debug=True)

    # Run this locally and then go to browser http://127.0.0.1:5000/
    # and you can open http://127.0.0.1:5000/ or http://127.0.0.1:5000/home
    # and http://127.0.0.1:5000/about
    # to see the respective pages

    # Any change to the above functions are refected real time in the 
    # browser when you just refresh the page! 