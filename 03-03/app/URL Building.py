from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return 'index'

@app.route('/login')
def login():
    return 'login'

@app.route('/user/<username>')
def profile(username):
    return '{}\'s profile'.format('escape'(username))

with app.test_request_context():
    print('url_for'('index'))
    print('url_for'('login'))
    print('url_for'('login', next='/'))
    print('url_for'('profile', username='John Doe'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if 'request'.method == 'POST':
        return 'do_the_login'()
    else:
        return 'show_the_login_form'()

# membuat kondisional
if __name__ == "__main__":
    app.run()