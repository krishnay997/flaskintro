from flask import Flask,render_template
app = Flask(__name__)

@app.route("/")
def index():
   return render_template('index.html')


@app.route('/user/<username>')
def show(username):
    return f"Hi {username[0:8]}"

if __name__ == '__main__': # Revisit previous challenge if you're uncertain what this does https://code.nextacademy.com/lessons/name-main/424
   app.run()