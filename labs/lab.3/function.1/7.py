def has3(n):
    for i in range(len(n) - 1):
        if n[i] == 3 and n[i + 1] == 3: 
            return True 
    return False 
n = list(map(int, input().split()))
print(has3(n))
