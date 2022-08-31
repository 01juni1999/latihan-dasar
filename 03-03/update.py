try:
    import psycopg2
    conn = psycopg2.connect(
        host="localhost",
        database="contoh",
        user="postgres",
        password="PPQS0106")
        
    curs = conn.cursor()

    namalama = "rahma"
    
    namabaru = "rahmi"
    umurbaru= 27
    query= f"update siswa set nama='{namabaru}', umur={umurbaru} where nama='{namalama}'"

    curs.execute(query)
    conn.commit()
    print("data berhasil di update")

except Exception as e :
    print(e)