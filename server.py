from flask import Flask
app = Flask(__name__)

@app.route("/") # Revisit decorators if you unclear of this syntax
def index():
    return '<h1>Why so easy peasy</h1>'


@app.route('/user/<username>')
def show(username):
    return f"Hi {username[0:8]}"

if __name__ == '__main__': # Revisit previous challenge if you're uncertain what this does https://code.nextacademy.com/lessons/name-main/424
   app.run()