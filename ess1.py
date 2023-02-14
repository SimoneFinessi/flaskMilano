from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def home():
  return render_template("home.html", Titolo='Welcome', Testo='Hello, world!')

@app.route('/immagini')
def hello_world():
  return render_template("immagini.html", Titolo='Welcome', Testo='Hello, world!')

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)