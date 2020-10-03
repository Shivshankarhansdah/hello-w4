from flask import Flask, render_template
from db.model import ModelSQLite

app = Flask(__name__)

model = ModelSQLite()
results = model.get_all_items()


@app.route('/')
def index():
  """
  Home page. Load index.html
  """
  return render_template("index.html",
    data=results,
    title='Elit Hunter')


if __name__ == '__main__':
  app.run()
