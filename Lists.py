N = int(input("giriniz : "))

inputs = []


for i in range(0,N):
    inp = input().split()
    if inp[0] == "insert":
        inputs.insert(int(inp[1]),int(inp[2]))
    
    elif inp[0] == "print":
        print(inputs)
    
    elif inp[0] == "remove":
        inputs.remove(int(inp[1]))
    
    elif inp[0] == "append":
        inputs.append(int(inp[1]))
    
    elif inp[0] == "sort":
        inputs.sort()
        
    elif inp[0] == "pop":
        inputs.pop()
        
    else :
        inputs.reverse()