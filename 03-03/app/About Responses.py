from flask import Flask
app = Flask(__name__)

@app.errorhandler(404)
def not_found(error):
    return 'render_template'('error.html'), 404

@app.errorhandler(404)
def not_found(error):
    resp = 'make_response'('render_template'('error.html'), 404)
    resp.headers['X-Something'] = 'A value'
    return resp

if __name__ == "__main__":
    app.run()