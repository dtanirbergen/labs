def convert(value):
    if value.isdigit():  
        return int(value)  
    elif value.lower() in ["true", "false"]:  
        return value.lower() == "true"  
    else:
        return value

def all_true(t):
    return all(t)  

t = tuple(map(convert, input("Введите элементы: ").split()))

print(all_true(t))  
