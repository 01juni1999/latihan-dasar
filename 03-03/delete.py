try:
    import psycopg2
    conn = psycopg2.connect(
        host="localhost",
        database="contoh",
        user="postgres",
        password="PPQS0106")
        
    curs = conn.cursor()

    nama = "rahmi"
    query= f"delete from siswa  where nama='{nama}'"
    curs.execute(query)
    conn.commit()
    print("data berhasil di delete!")

except Exception as e :
    print(e)