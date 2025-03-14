import re
with open(r'C:\Users\user\Desktop\PP_2\lab.5\text.txt') as file:
    text = file.read() 
result = re.sub(r'_(\w)', lambda m: m.group(1).upper(), text)
result = result[0].upper() + result[1:] 
print(result) 