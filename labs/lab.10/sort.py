import psycopg2
from config import load_config

def sort(conn):
    command = "SELECT id, name, phone FROM students ORDER BY name ASC"
    with conn.cursor() as cur:
        cur.execute(command)
        rows = cur.fetchall()
        for row in rows:
            print(f"ID: {row[0]}, Name: {row[1]}, Phone: {row[2]}")

if __name__ == '__main__':
    try:
        config = load_config()
        with psycopg2.connect(**config) as conn:
            sort(conn)

    except (psycopg2.DatabaseError, Exception) as error:
        print("Error:", error)