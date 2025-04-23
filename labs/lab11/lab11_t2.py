import psycopg2
from config import load_config

def insert_or_update_user(name, phone):
    command = "CALL insert_or_update_user(%s, %s)"
    try:
        config = load_config()
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                cur.execute(command, (name, phone))
                conn.commit()
    except (psycopg2.DatabaseError, Exception) as error:
        print("error", error)

if __name__ == '__main__':
    name = input("Enter name: ")
    phone = input("Enter phone: ")
    insert_or_update_user(name, phone)

"""
CREATE OR REPLACE PROCEDURE insert_or_update_user(username TEXT, userphone TEXT)
LANGUAGE plpgsql
AS $$
BEGIN
    IF EXISTS (SELECT 1 FROM students WHERE name = username) THEN
        UPDATE students SET phone = userphone WHERE name = username;
    ELSE
        INSERT INTO students(name, phone) VALUES (username, userphone);
    END IF;
END;
$$;
"""