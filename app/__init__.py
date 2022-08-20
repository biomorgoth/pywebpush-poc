import flask
import http
import os
import pywebpush

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

@app.post("/push/subscribe")
def push_subscribe():
    """
    Receives a Web Push subscription and stores it.
    """
    # Take in mind this is a test project and the subscription should be stored in a database,
    # with its corresponding business associations/relations.
    flask.session['push_subscription'] = flask.request.get_json()
    return flask.make_response('', http.HTTPStatus.NO_CONTENT)

@app.post("/push/send")
def push_send():
    """
    Tries to send a WebPush message and responds 204 or 500 depending on the result.
    """
    # Example from: https://pypi.org/project/pywebpush/
    try:
        pywebpush.webpush(
            subscription_info=flask.session['push_subscription'],
            data='Mary had a little lamb, with a nice mint jelly',
            vapid_private_key=os.environ['PRIVATE_KEY_DER'],
            vapid_claims={
                    'sub': 'mailto:{}'.format(os.environ['WEBPUSH_MAILTO']),
                }
        )

        return flask.make_response('', http.HTTPStatus.NO_CONTENT)
    except pywebpush.WebPushException as ex:
        print("I'm sorry, Dave, but I can't do that: {}", repr(ex))
        # Mozilla returns additional information in the body of the response.
        if ex.response and ex.response.json():
            extra = ex.response.json()
            print("Remote service replied with a {}:{}, {}",
                extra.code,
                extra.errno,
                extra.message
                )
        return flask.make_response('', http.HTTPStatus.INTERNAL_SERVER_ERROR)
