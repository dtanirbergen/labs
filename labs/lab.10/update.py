import psycopg2
from config import load_config

def update_user_by_id(conn, id, new_name, new_phone):
    command = "UPDATE students SET name = %s, phone = %s WHERE id = %s"
    with conn.cursor() as cur:
        cur.execute(command, (new_name, new_phone, id))
    conn.commit()
    print("Updated successfully!")

if __name__ == '__main__':
    try:
        config = load_config()
        with psycopg2.connect(**config) as conn:
            id = int(input("enter id: "))
            new_name = input("enter new name: ")
            new_phone = input("enter new phone: ")
            update_user_by_id(conn, id, new_name, new_phone)

    except (psycopg2.DatabaseError, Exception) as error:
        print("error", error)