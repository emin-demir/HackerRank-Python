import textwrap

def wrap(string, max_width):
   
        
    return textwrap.fill(string,max_width)
    

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)


#-------------------------------------------------------------------------


# import textwrap

# def wrap(string, max_width):
#     text1 = []
#     l = 0
#     for i in range(int(len(string)/max_width)+1):
        
#         text1 += string[l:l+max_width]
#         l += max_width
    
#     return textwrap.fill(string,max_width)

# if __name__ == '__main__':
#     string, max_width = input(), int(input())
#     result = wrap(string, max_width)
#     print(result)