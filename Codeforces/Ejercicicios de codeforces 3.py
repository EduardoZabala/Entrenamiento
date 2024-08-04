"""
#A. Dubstep
s=input().split("WUB")
print(" ".join(s))
"""
"""
#A. String Task
s=input().lower()
vocales=["a","e","i","o","u","y"]
cadena=[]
for i in s:
    if i not in vocales:
        cadena.append(".")
        cadena.append(i)
print("".join(cadena))
"""
"""
#A. Young Physicist
n=int(input())
comprobacion=True
num1=[]
num2=[]
num3=[]

for _ in range(n):
    a,b,c=map(int,input().split())
    num1.append(a)
    num2.append(b)
    num3.append(c)
sum1=sum(num1)
sum2=sum(num2)
sum3=sum(num3)
if sum1!=0:
    comprobacion=False 
elif sum2!=0:
    comprobacion=False
elif sum3!=0:
    comprobacion=False
if comprobacion==True:
    print("YES")
else: 
    print("NO")
"""
"""
Problema de codewars 
numbers= input().split(",")
numbers=[int(x) for x in numbers]
contador=[]
print(numbers)
count=0
i=len(numbers)-1
while count<i:
    if numbers[count]< numbers[count+1]:
        contador.append(numbers[count])
    count+=1
numbers.remove(min(contador))
print(numbers)
"""
"""
#primera condicion el numero debe quedar distinto a un cero en el principio
#si minus es 0 se devuelve el numero

def quitador_numeros(valor):
    global minus,num
    array_num=[]
    num=str(num)
    if minus!=0:
        for iterador in range(valor):
            if num[iterador]!=0:
                array_num.append(num[iterador])
        array_num=[str(x) for x in array_num]
        return "".join(array_num)
    else:
        return num

t=int(input())
while t>0:
    num=int(input())
    minus=int(input())
    long=len(str(num))-minus
    print(quitador_numeros(long))
    t-=1

#print(numbers,remove_smallest(numbers))
"""

#primero cambiar dos numeros (debo buscar el lugar del numero y intercambiarlo con el otro numero)
#segundo eliminar el ultimo digito
#numero=[2,3,4,1,5,6] # [3,4,2,5]
                   #    0 1 2 3
#numero=[4,8,7,4,5,6,3,9,8]
def intercambiador(lista_numero):
    longitud=len(lista_numero)-1
    numero_pequeño=min(lista_numero)
    
    while longitud>=1:
        indice=lista_numero.index(numero_pequeño)
        if indice!=0:
            aux=lista_numero[indice-1]
            lista_numero[indice-1]=numero_pequeño
            lista_numero[indice]=aux
            lista_numero.pop(longitud) 
        else:
            aux_indice=indice+1
            aux_numero=lista_numero[aux_indice]
            lista_numero[aux_indice]=lista_numero[indice]
            lista_numero[indice]=aux_numero
            lista_numero.pop(longitud)
        longitud-=1
    return lista_numero[0]
n=int(input())
while n>0:
    n-=1
    numero=input()
    lista_numero=[int(x) for x in numero]
    print(intercambiador(lista_numero))

        