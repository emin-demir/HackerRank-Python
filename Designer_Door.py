row, column = map(int, input().split())
line = "-"
tsk = ".|."
string = "WELCOME"

m = 1
plus_eksi = 3
plus_tsk = 2
string_length = len(string)

s = int((row - 1) / 2)
length = int((column - 3) / 2)
out_string_length = int((column - string_length) / 2)

for i in range(s):
    print(line * length + tsk * m + line * length)
    length -= plus_eksi
    m += plus_tsk
    if length < plus_eksi:
        break
    
print(line * out_string_length + string + line * out_string_length)

for i in range(s):
    m -= plus_tsk
    length += plus_eksi
    print(line * length + tsk * m + line * length)
    if m == plus_tsk:
        break    
