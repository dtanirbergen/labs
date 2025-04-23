import psycopg2
from config import load_config
import csv

def insert(conn, name, phone):
    command = """INSERT INTO students(name,phone) VALUES(%s, %s)"""
    with conn.cursor() as cur:
        cur.execute(command, (name, phone))
    conn.commit()

def insert_student_from_csv(conn, csv_file_name):
    command = "INSERT INTO students(name,phone) VALUES(%s, %s)"
    with conn.cursor() as cur:
        with open(csv_file_name, "r", encoding="utf-8") as csvfile:
            csvreader = csv.reader(csvfile, delimiter=',')
            next(csvreader) 
            for row in csvreader:
                name, phone = row
                cur.execute(command, (name, phone))
    conn.commit()

if __name__ == '__main__':
    try:
        config = load_config()
        with psycopg2.connect(**config) as conn:
            insert_student_from_csv(conn, r"C:\Users\user\Desktop\PP_2\labs\lab.10\contacts.csv") 
            name = input("Enter name: ")
            phone = input("Enter phone: ")
            insert(conn, name, phone)

    except (psycopg2.DatabaseError, Exception) as error:
        print("error", error)