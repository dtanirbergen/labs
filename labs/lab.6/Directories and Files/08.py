import os 
path =input("text: ")
if os.path.exists(path):  
    os.remove(path)  
    print(f"file {path} deleted!")  
else:
    print(f"file {path} not found!") 