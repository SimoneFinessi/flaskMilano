from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def home():
  return render_template("home.html", Titolo='HOME')

@app.route('/immagini')
def hello_world():
  return render_template("immagini.html", Titolo='immagini')
@app.route('/duomo')
def duomo():
  return render_template("duomo.html", Titolo='duomo')

@app.route('/castello')
def castello():
  return render_template("castello.html", Titolo='castello')

@app.route('/brera')
def brera():
  return render_template("brera.html", Titolo='brera')

@app.route('/vittorio')
def vittorio():
  return render_template("vittorio.html", Titolo='vittorio')


if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)