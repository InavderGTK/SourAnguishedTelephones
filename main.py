
3
4
5
6
7
8
9
10
11
12
13
14
15
 
s = int(input("Sayı girin: "))  
f = 0
i = 2
while i <= s / 2:
    if s % i == 0:
        f=1
        break
    i=i+1
    
if f==0:
    print("Asal Sayıdır")
else:
    print("Asal Sayı Değildir")
    