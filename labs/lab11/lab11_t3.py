import psycopg2
from config import load_config

def insert_many_users(names, phones):
    try:
        config = load_config()
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                cur.execute("CALL insert_many_users(%s, %s)", (names, phones))
                print("\nDone. Check pgAdmin console for invalid data.")
    except Exception as e:
        print("error:", e)

if __name__ == '__main__':
    names_input = input("Enter names separated by commas: ")
    phones_input = input("Enter phones separated by commas: ")
    names = [n.strip() for n in names_input.split(',')]
    phones = [p.strip() for p in phones_input.split(',')]
    insert_many_users(names, phones)

"""
CREATE PROCEDURE insert_many_users(names TEXT[], phones TEXT[])
LANGUAGE plpgsql
AS $$
DECLARE
    i INT;
BEGIN
    FOR i IN 1..array_length(names, 1) LOOP
        IF phones[i] ~ '^\d+$' THEN
            INSERT INTO students(name, phone)
            VALUES (names[i], phones[i]);
        ELSE
            RAISE NOTICE 'Invalid: % - %', names[i], phones[i];
        END IF;
    END LOOP;
END;
$$;
"""