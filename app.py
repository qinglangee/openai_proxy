
from flask import Flask, render_template, request
import ai_query as ai
import file_util
import datetime as dt

import time

app = Flask(__name__)

@app.route('/')
def hello_world():
    datestr = file_util.read_root_file('final_date')
    date = dt.datetime.strptime(datestr, '%Y-%m-%d')
    num = (date - dt.datetime.now()).days
    return render_template('index.html', date=datestr, num=num)


@app.route('/query')
def query():

    return ai.query("what time?")

@app.route('/query/<content>')
def query_arg(content):

    return ai.query(content)


@app.post('/ask')
def ask():
    content = request.form['content']
    return ai.query(content)

@app.route('/updatedate/<date>')
def update_date(date):
    file_util.write_root_file('final_date', date)
    return date
    


# run the app.
if __name__ == "__main__":
    # Setting debug to True enables debug output. This line should be
    # removed before deploying a production app.
    app.debug = True
    app.run()