import psycopg2
from psycopg2 import Error

# Подключение к базе данных
conn = psycopg2.connect(
    database="phonebook",  # Название вашей базы данных
    user="postgres",       # Ваше имя пользователя
    password="Dim@sh07",   # Ваш пароль
    host="localhost",      # Хост (локально или сервер)
    port="5432"            # Порт по умолчанию для PostgreSQL
)

cur = conn.cursor()

# Функция для удаления контакта по имени или телефону
def delete_by_name_or_phone():
    value = input("Введите имя или телефон для удаления: ")  # Запрашиваем имя или телефон для удаления
    try:
        # Вызов процедуры для удаления
        cur.execute("CALL delete_student_by_name_or_phone(%s)", (value,))
        conn.commit()  # Подтверждение изменений в базе
        print("Контакт удален.")  # Выводим сообщение о успешном удалении
    except Error as e:
        print(f"Ошибка базы данных: {e}")  # Ошибка, если что-то пошло не так
        conn.rollback()  # Откат транзакции в случае ошибки

# Функция для отображения меню
def menu():
    run = True
    while run:
        print("\nМЕНЮ PHONEBOOK:")
        print("1 - Удалить контакт по имени или телефону")
        print("2 - Выход")

        choice = input("Введите ваш выбор (1-2): ")

        if choice == '1':
            delete_by_name_or_phone()  # Вызов функции удаления
        elif choice == '2':
            run = False  # Завершаем программу
        else:
            print("Некорректный выбор. Попробуйте снова.")  # Ошибка выбора

if __name__ == "__main__":
    try:
        menu()  # Запускаем меню
    except Error as e:
        print(f"Ошибка базы данных: {e}")  # Ошибка подключения или выполнения
    finally:
        cur.close()  # Закрываем курсор
        conn.close()  # Закрываем подключение
