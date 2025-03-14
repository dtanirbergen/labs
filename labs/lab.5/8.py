import re
with open(r'C:\Users\user\Desktop\PP_2\lab.5\text.txt') as file:
    text = file.read() 
print(re.findall(r'[A-Z][a-z]*', text))