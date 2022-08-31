
from flask import Flask
app = Flask(__name__)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if"request".method == 'POST':
        return "do_the_login"()


    if __name__ =="__main__":
        app.run()
