filename = input("Название: ")
with open (filename, "r", encoding="utf-8") as file:
    first = file.readlines().strip()
    print(first)