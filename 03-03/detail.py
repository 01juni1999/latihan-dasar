try:       
    import psycopg2
    conn = psycopg2.connect(
        host="localhost",
        database="contoh",
        user="postgres",
        password="PPQS0106")
    
except Exception as e:
    print(e)

curs = conn.cursor()
query= f"select * from siswa where umur =23" #where berarti menampilkan data yamg ditail
curs.execute(query)
data= curs.fetchone()

if not data:
    print("gaada say")
else:
    print("nama:", data[0], "umur:", data[0])





