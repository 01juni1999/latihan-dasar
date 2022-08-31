from flask import Flask
app = Flask(__name__)

@app.route("/")
def index():
    return"halaman index"

@app.route('/hello') 
def hello():
    return"hello loooo"

#menampilkan nama pengguna
@app.route('/user/<user_name>')
def show_user_profil(user_name):
    return"hello, naila"

@app.route('/post/<int:post_id>')
def show_post(post_id):
    return f'Post{post_id}'


# membuat kondisional untuk running dan mendapatkan link
if __name__ == "__main__":
    app.run()