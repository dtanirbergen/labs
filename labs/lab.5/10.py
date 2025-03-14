import re
with open(r'C:\Users\user\Desktop\PP_2\lab.5\text.txt') as file:
    text = file.read() 
r=re.sub(r'([a-z])([A-Z])',r'\1_\2',text).lower()
print(r) 