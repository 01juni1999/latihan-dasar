from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    username = 'request'.cookies.get('username')
    # use cookies.get(key) instead of cookies[key] to not get a
    # KeyError if the cookie is missing.

@app.route('/')
def index():
    resp = 'make_response'('render_template'(...))
    resp.set_cookie('username', 'the username')
    return resp

if __name__ =="__main__":
    app.run()