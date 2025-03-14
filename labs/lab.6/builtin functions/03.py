def is_palindrome(txt):
    txt = txt.replace(" ", "").lower()
    return txt == txt[::-1]

text = input("Введите текст: ")
if is_palindrome(text):
    print("палиндром")
else:
    print("не палиндром")
