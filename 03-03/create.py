try:
    import psycopg2
    conn = psycopg2.connect(
        host="localhost",
        database="contoh",
        user="postgres",
        password="PPQS0106")
        
    curs = conn.cursor()
    nama = "rahma"
    umur = "26"
    query= f"insert into siswa(nama,umur) values('{nama}',{umur})"

    curs.execute(query)
    conn.commit()
    print("data masuk")

except Exception as e :
    print(e)