import psycopg2
from config import load_config

def create_table():
    command = """
        CREATE TABLE students (
            id SERIAL PRIMARY KEY,
            name VARCHAR(255) NOT NULL,
            phone VARCHAR(20) NOT NULL
        )
    """
    try:
        config = load_config()
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                cur.execute(command)
                conn.commit()
    except (psycopg2.DatabaseError, Exception) as error:
        print("error", error)

if __name__ == '__main__':
    create_table()