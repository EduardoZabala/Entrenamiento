"""
# A. Boy or Girl
s=input()
letter=[]
for vocal in s:
    if vocal not in letter:
        letter.append(vocal)
if len(letter)%2==0:
    print("CHAT WITH HER!")
else:
    print("IGNORE HIM!")
"""
"""
#A. Stones on the Table
longitud=int(input())
s=input()
n=0
count=0
letter=[str(x) for x in s ]
    
while n<longitud-1:
    if letter[n]==letter[n+1]:
        count+=1

    n+=1
print(count)
"""

"""
#A. Bear and Big Brother
a,b=map(int,input().split())
veces=0
while a<=b:
    a*=3
    b*=2
    veces+=1
print(veces)
"""
"""
#A. Bear and Big Brother
import math
m,n,a=map(int,input().split())
valor1=math.trunc(m/a)
valor2=math.trunc(n/a)
if m%a!=0 and m!=a:
    valor1+=1
if n%a!=0 and n!=a:
    valor2+=1
print(valor1*valor2)
"""
"""
#A. Soldier and Bananas
#n=número de dolares que tiene el soldado
#k=los dolares que paga por la primera banana
#w= son los bananos que quiere comprar
k,n,w=map(int,input().split()) 
counter=0
sum=0
while counter<w:
    counter+=1
    x=k*counter
    sum+=x
if n-sum<0:
    print(abs(n-sum))
else:
    print(0)
"""
"""
#A. Elephant
import math
steps=int(input())
resp=math.trunc(steps/5)
if steps%5!=0:
    resp+=1
print(resp)
"""

"""
# A. Word
s1=input()
count_up=0
count_low=0
for i in s1:
    if i.isupper()==True: #isupper=sirve para comprobar si un letra es mayuscula 
                          #o minuscula;arroja "true" si es mayuscula
        count_up+=1
    else:
       count_low+=1
if count_up>count_low:
    print(s1.upper())
else:
    print(s1.lower())
"""
"""
# A. Wrong Subtraction
import math
num,times=map(int,input().split())
rep=0
while rep<times:
    if num%10==0:
        num/=10
    else:
        num-=1
    rep+=1
print(math.trunc(num))
"""
"""
num = input()
numlist = list(num)
num = 0
for i in range(len(numlist)):
    if(numlist[i] == '4' or numlist[i] == '7'):
        num += 1

numlist = list(str(num))

lucky = True
for i in range(len(numlist)):
    if(numlist[i] != '4' and numlist[i]!= '7'):
        lucky = False

if(lucky):
    print("YES")
else:
    print("NO")
"""
"""
#A. Anton and Danik
n=int(input())
s=input()
count_a=0
count_d=0

for i in s:
    if i=="A":
        count_a+=1
    elif i=="D":
        count_d+=1
if count_a>count_d:
    print("Anton")
elif count_a<count_d:
    print("Danik")
else:
    print("Friendship")

"""
"""
#A. Translation
s1=input().lower()
s2=input().lower()
"""
"""
#Tiempo= 124 ms
s1_l=[str(x) for x in s1]
s2_l=[str(x) for x in reversed(s2)]
if (s1_l==s2_l):
    print("YES")
else:
    print("NO")
"""
"""
#Tiempo=216 ms
comprobador=len(s1)
for i in range(0,len(s1)):
   if s1[i]!=s2[len(s2)-i-1]:
       #print(s1[i],s2[len(s2)-i-1])
        comprobador-=1
if comprobador!=len(s1):
    print("NO")
else:
    print("YES")
"""
"""
import math
t=int(input())
while t>0:
    n=int(input())
    if n%2!=0:
        operation=n-1
        print(f"1 {operation}")
    else:
        operation=math.trunc(n/2)
        print(f"{operation} {operation}")
    t-=1

"""
"""
#   M. Minimum LCM
for _ in range(int(input())): #codigo que fue aceptado pero no es de mi autoria
    n = int(input())
    i=2
    m=1
    while i**2 <=n:
        if n%i==0:
            m = n//i if n//i >m else m
        
        i+=1
    print(m, n-m)        
# Codigo mio que no fue aceeptado pero sin funciona

t=int(input())
while t>0:
    n=int(input())
    if n%2!=0:
        operation=n-1
        print(f"1 {operation}")
    else:
        operation=n//2
        print(f"{operation} {operation}")
    t-=1
"""







