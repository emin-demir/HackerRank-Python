def swap_case(s):
    letter = ""
    for i in s:
        if i == i.upper():
            letter += i.lower()
        else :
            letter += i.upper()
    return letter

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)