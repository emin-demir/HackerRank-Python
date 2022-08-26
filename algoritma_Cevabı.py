liste = [10,9,8,7,6,5,4,3,2,1]

n = int(input())

len_liste = len(liste)

mod = n % len_liste  
print("mod : ", str(mod))

if mod == 0 :
      print(liste)
      
else:
      for i in range(n) :
            son_eleman = liste[len(liste) - 1]
            for i in range(len_liste):
                  liste[len_liste - 1  - i] = liste[len_liste - 2  - i]
            liste[0] = son_eleman         
      print(liste)