import flask
import os

application_server_key = os.environ['APPLICATION_SERVER_KEY']

app = flask.Flask(__name__)

@app.route("/")
def index():
    return flask.render_template('index.html', application_server_key=application_server_key)
