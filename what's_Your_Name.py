def print_full_name(first_name, last_name):
   hi = "Hello {first} {last}! You just delved into python".format(first=first_name, last=last_name)
   print(hi)

if __name__ == '__main__':
    first_name = str(input())
    last_name = str(input())
    print_full_name(first_name, last_name)