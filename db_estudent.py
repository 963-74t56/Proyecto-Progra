import psycopg2

conn = psycopg2.connect(
    dbname="nombre_bd",
    user="usuario",
    password="contraseña",
    host="localhost",
    port="5432"
)
cursor = conn.cursor()
cursor.execute("SELECT * FROM estudiantes")

