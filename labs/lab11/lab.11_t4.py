import psycopg2
from psycopg2 import Error

# Подключение к базе данных
conn = psycopg2.connect(
    database="phonebook",  # Название вашей базы данных
    user="postgres",       # Ваш логин в PostgreSQL
    password="Dim@sh07",   # Ваш пароль для подключения к PostgreSQL
    host="localhost",      # Хост базы данных (обычно 'localhost')
    port="5432"            # Порт PostgreSQL (по умолчанию 5432)
)

# Создание курсора
cur = conn.cursor()

# Функция для выполнения запроса с пагинацией
def query_paginated():
    limit = int(input("Введите лимит (количество записей на странице): "))
    offset = int(input("Введите смещение (для определения страницы): "))
    
    try:
        # Выполнение запроса к функции get_paginated_students с параметрами limit и offset
        cur.execute("SELECT * FROM get_paginated_students(%s, %s)", (limit, offset))
        rows = cur.fetchall()
        
        # Печать результатов
        if rows:
            print(f"\nПоказываем {limit} записей, начиная с {offset + 1} (смещение):")
            for row in rows:
                print(f"ID: {row[0]}, Имя: {row[1]}, Телефон: {row[2]}")
        else:
            print("Записи не найдены.")
    
    except Error as e:
        print(f"Ошибка при выполнении запроса: {e}")

# Основное меню
def menu():
    run = True
    while run:
        print("\nМЕНЮ:")
        print("1 - Показать контакты с пагинацией")
        print("2 - Выход")
        
        choice = input("Введите ваш выбор (1-2): ")
        
        if choice == '1':
            query_paginated()
        elif choice == '2':
            run = False
        else:
            print("Некорректный выбор. Попробуйте снова.")

if __name__ == "__main__":
    try:
        menu()
    except Error as e:
        print(f"Ошибка базы данных: {e}")
    finally:
        # Закрытие соединения с базой данных
        cur.close()
        conn.close()
