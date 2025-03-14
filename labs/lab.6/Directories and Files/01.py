import os

def list_directory(path):
    try:
        items = os.listdir(path)
        only_dir = [item for item in items if os.path.isdir(os.path.join(path, item))] 
        only_file = [item for item in items if os.path.isfile(os.path.join(path, item))]
        
        print("Directories:")
        print(only_dir)
        print("\nFiles:")
        print(only_file)
        print("\nAll items:")
        print(items)
    
    except FileNotFoundError:
        print("Error: Path does not exist")
    except PermissionError:
        print("Error: You don't have permission to access this directory")

path = input("Enter a path: ")
list_directory(path)
