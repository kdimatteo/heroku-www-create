
import flask
import os
from functools import wraps


app = flask.Flask(__name__)


def check_auth(username, password):
    """
    This function is called to check if a username / password combination is valid.
    """
    return username == 'admin' and password == 'Adm1n'


def authenticate():
    """Sends a 401 response that enables basic auth"""
    return flask.Response('Could not verify your access level for that URL.\nYou have to login with proper credentials', 401, {'WWW-Authenticate': 'Basic realm="Login Required"'})


def requires_auth(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        auth = flask.request.authorization
        if not auth or not check_auth(auth.username, auth.password):
            return authenticate()
        return f(*args, **kwargs)
    return decorated


@app.route("/")
@requires_auth
def default():
	return home("./html/index.html")

@app.route("/<path:filename>")
def passThrough(filename):
        return flask.send_from_directory("./html", filename);


if __name__ == "__main__":
	# Bind to PORT if defined, otherwise default to 5000.
	port = int(os.environ.get('PORT', 5000))
	app.run(host='0.0.0.0', port=port, debug=True)