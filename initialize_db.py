import sqlite3

def ejecutar_script_sql(archivo_sql, db_path='databases/productos.db'):
    # Leer el archivo SQL
    with open(archivo_sql, 'r') as file:
        script_sql = file.read()

    # Conectar a la base de datos SQLite
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # Ejecutar el script SQL
    try:
        cursor.executescript(script_sql)
        print("Script ejecutado con éxito")
    except sqlite3.Error as e:
        print(f"Error al ejecutar el script: {e}")
    finally:
        cursor.close()
        conn.close()

if __name__ == "__main__":
    ejecutar_script_sql('databases/script.sql')
