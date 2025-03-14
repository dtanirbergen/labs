import re
with open(r'C:\Users\user\Desktop\PP_2\lab.5\text.txt') as file:
    text = file.read() 
print(re.findall(r'ab{2,3}', text))  