from flask import Flask
from flask import render_template
from helpers.breaches import read_spreadsheet, find_breaches_by_state, find_breach_by_id

from os.path import exists

app = Flask(__name__)

@app.route("/hello")
def helloworld():
    return render_template('hello.html')

@app.route("/")
def homepage():
    return render_template('index.html')

@app.route("/breaches")
def breaches():
    return render_template('breaches.html', breaches=read_spreadsheet())

@app.route("/state/<state>")
def by_state(state):
    return render_template('state.html',
                    state=state,
                    breaches=find_breaches_by_state(state))

@app.route("/breaches/<id>")
def by_id(id):
    return render_template('breach.html',
                    breach=find_breach_by_id(id))



if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)
