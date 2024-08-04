"""
#
entrada = input()
lista = entrada.split(' ')
altura = int(lista[0])
base = int(lista[1])
calculador=float(altura*base)/2
"""
"""
# A. Petya and Strings
s2,s1=input(),input()
s1=s1.lower()
s2=s2.lower()

#s1="s"
#s2="z"
n=0
res=0

while n<len(s1):
    if s1[n]>s2[n]:
        res=1
        break
    elif s1[n]<s2[n]:
        res=-1
        break 
    n+=1
print(res)    
"""
"""
#Bit ++
x=0
n=int(input()) #2
i=0
while n>i:
    s1=input()
    if s1[1]=="+":
        x+=1
    else:
        x-=1

    i+=1
print(x)
"""
"""
# A. Próxima ronda
People,Winers=map(int,input().split()) 
arr=list(map(int,input().split())) 

counter=0
for i in range(0,People): 
    if arr[Winers-1]==0 and arr[i] == arr[Winers-1]: 
        counter+=0 
    elif arr[Winers-1]<=arr[i]: 
        counter+=1 
    else: 
        counter+=0 
print(counter)
"""
"""
#A. Helpful Maths

a=list(map(int,input().split("+")))
a.sort()
string_a=[str(i) for i in a]
print("+".join(string_a))
"""
"""
#A. Word Capitalization
n=0
Capitalizadas=[]
c=Palabra[0].upper()
Capitalizadas.append(c)
while n<len(Palabra)-1:
    n+=1
    Capitalizadas.append(Palabra[n])
print("".join(Capitalizadas))
"""
# A. Beautiful Matrix
a=[int(x) for x in input().split()]
b=[int(x) for x in input().split()]
c=[int(x) for x in input().split()]
d=[int(x) for x in input().split()]
e=[int(x) for x in input().split()]

if sum(a)!=0:
    columna,fila=1,a.index(1)+1
elif sum(b)!=0:
    columna,fila=2,b.index(1)+1
elif sum(c)!=0:
    columna,fila=3,c.index(1)+1
elif sum(d)!=0:
    columna,fila=4,d.index(1)+1
else:
    columna,fila=5,e.index(1)+1 #index sirve para encontrar la posición del valor
                                #abs() sirve para encontrar el valor absoluto de un número


r,c=3,3 # r y c son los valores del punto en el centro
print(abs(columna-r)+abs(c-fila)) #se suman los dos puntos y nos da la distancia menor, se utiliza la formula de 
                                   # encontrar la distancia de dos puntos
"""
0 0 0 0 1 #posicion de fila es=1 y columna es 5
0 0 0 0 0
0 0 0 0 0
0 0 0 0 0
0 0 0 0 0
"""