from flask import Flask
from flask import render_template
from flask import request, redirect
import psycopg2

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")
    conn = psycopg2.connect(
        host="localhost",
        database="contoh",
        user="postgres",
        password="PPQS0106"
    )
    curs = conn.cursor()
    if request.method == "POST":
        nama=request.form["nama"]
        detail=request.form["detail"]
        query = f"insert into buah(nama, detail) values('{nama}', '{detail}')"
        curs.execute(query)
        conn.commit()
        
    print(request.method)
    query = f"select * from buah"
    curs.execute(query)
    data = curs.fetchall()
    curs.close()
    conn.close()
     # data = ["aple", "pear", "anggur"]
    return render_template("index.html", context=data)


@app.route("/post")
def detail():
    return render_template("detail.html")

@app.route("/about")
def update():
    return render_template("update.html")


if __name__ == "__main__":
    app.run()