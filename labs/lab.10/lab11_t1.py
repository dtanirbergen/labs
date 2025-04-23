import psycopg2
from config import load_config

def search_by_pattern(pattern):
    command = """
        SELECT * FROM students
        WHERE name ILIKE %s OR phone ILIKE %s
    """
    try:
        config = load_config()
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                search = f"%{pattern}%"
                cur.execute(command, (search, search))
                rows = cur.fetchall()
                for row in rows:
                    print(row)
    except (psycopg2.DatabaseError, Exception) as error:
        print("error", error)

if __name__ == '__main__':
    pattern = input("Enter search pattern: ")
    search_by_pattern(pattern)