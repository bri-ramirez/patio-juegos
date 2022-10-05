from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def home():
    return "Hola Mundo!!"

@app.route('/play')
def play():
    return render_template("index.html", repeat=3, color="blue")

@app.route('/play/<int:repeat>')
def play2(repeat):
    return render_template("index.html", repeat=repeat, color="blue")

@app.route('/play/<int:repeat>/<color>')
def play3(repeat, color):
    return render_template("index.html", repeat=repeat, color=color)

if __name__=="__main__":
    app.run(debug=True) 