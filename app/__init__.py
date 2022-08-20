import flask
import http
import os

application_server_key = os.environ['APPLICATION_SERVER_KEY']

app = flask.Flask(__name__)
# Enable Flask sessions with this. See: https://flask.palletsprojects.com/en/2.1.x/api/#flask.session
app.config['SECRET_KEY'] = os.environ['SECRET_KEY']

@app.get("/")
def index():
    """
    This controller just returns the homepage HTML.
    It is served from a controller since it does have certain data we would not like to hardcode for this example
    (i.e. the applicationServerKey)
    """
    return flask.render_template('index.html', application_server_key=application_server_key)

@app.post("/push_subscribe")
def push_subscribe():
    """
    Receives a Web Push subscription and stores it.
    """
    # Take in mind this is a test project and the subscription should be stored in a database,
    # with its corresponding business associations/relations.
    flask.session['push_subscription'] = flask.request.get_json()
    return flask.make_response('', http.HTTPStatus.NO_CONTENT)
