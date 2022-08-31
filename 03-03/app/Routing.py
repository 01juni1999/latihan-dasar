from flask import Flask
app = Flask(__name__)

@app.route("/")
def index():
    return"halaman index"

@app.route('/hello') 
def hello():
    return"hello loooo"

# membuat kondisional
if __name__ == "__main__":
    app.run()