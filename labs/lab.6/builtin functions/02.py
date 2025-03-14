def count_case(txt):
    upper = sum(map(str.isupper, txt))  
    lower = sum(map(str.islower, txt))  
    return upper, lower  

text = input("Ввод текста: ")
upper, lower = count_case(text)

print("Большие буквы: ", upper)
print("Маленькие буквы: ", lower)
