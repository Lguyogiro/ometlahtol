import glob
import random
from os.path import basename
from flask import Flask, render_template, session, request, flash
import pandas as pd

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('main.html')

@app.route('/practice', methods=['GET', 'POST'])
def practice():
    import pdb;pdb.set_trace()
    level = request.form['levels']
    possibilities = glob.glob('static/{}/*.jpg'.format(level))
    if not possibilities:
        flash("No words available yet for level {}".format(level))
        return render_template(index)
    else:
        options = [basename(pth).replace('.jpg', '')
                   for pth in random.sample(possibilities, 4)]
        selection = random.choice(options)

        return render_template("practice.html", word=selection, level=level, opts=options)

if __name__ == '__main__':
    app.run()