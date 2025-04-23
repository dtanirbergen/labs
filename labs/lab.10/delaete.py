import psycopg2
from config import load_config

def delete(conn, id):
    command = "DELETE FROM students WHERE id = %s"
    with conn.cursor() as cur:
        cur.execute(command, (id,))
    conn.commit()
    print(f"Deleted record with id: {id}")

if __name__ == '__main__':
    try:
        config = load_config()
        with psycopg2.connect(**config) as conn:
            id = input("enter id to delete: ")
            delete(conn, id)

    except (psycopg2.DatabaseError, Exception) as error:
        print("Error:", error)