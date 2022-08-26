girilen_input = int(input())
or_dict = {}
for i in range(girilen_input):
    malzemeler = input().split()
    malzeme = " ".join(malzemeler[:-1])
    fiyat = int(malzemeler[-1])
    
    if (or_dict.get(malzeme)):       
        or_dict[malzeme] += fiyat
    else:
        or_dict[malzeme] = fiyat
    
for i in or_dict:
    print(i, or_dict[i])

# from collections import OrderedDict

# girilen_input = int(input())
# or_dict = OrderedDict()
# for i in range(girilen_input):
#     malzeme = input().split()
#     fiyat = int(malzeme[-1])
#     isim = " ".join(malzeme[:-1])
#     if (or_dict.get(isim)):      
#         or_dict[isim] += fiyat
#     else:
#         or_dict[isim] = fiyat 
# for i in or_dict.keys():
#     print(i, or_dict[i])
