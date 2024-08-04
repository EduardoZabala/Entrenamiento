"""
year=int(input())
while True:
    year+=1
    a=year//1000
    b=year//100%10
    c=year//10%10
    d=year%10
    
    if a!=b and a!=c and a!=d and b!=c and b!=d and c!=d:
        break

print(year)
"""
"""
n=int(input())
PeopleAnswer=input().split(" ")
if PeopleAnswer[-1]=="0" and "1" not in PeopleAnswer:
    print("EASY")
else:
    print("HARD")
"""
"""
#A. George and Accommodation
rooms=int(input())
count=0
while rooms>0:
    p,c=map(int,input().split())
    if c-p>=2:
        count+=1
    rooms-=1
print(count)
"""
"""
coctels=int(input())
n=input().split()
nums=[int(x) for x in n]
print(sum(nums)/coctels)

"""
"""
s=input()
count=0

for i in range(len(s)-1):
    if s[i]==s[i+1]and s[i]==s[i+1+1]:
        count+=1

if count>=7:
    print('YES')
else:
    print('NO')
print(count)
"""
#A. Make it Beautiful #La logica esta correpta, pero falta cuadrarlo de acuerdo
                      #a los requerimientos de codeforces
"""
n=int(input())
while n>=0:
    n-=1
    x=int(input())
    array=list(map(int,input().split()))
    comprobador=[int(i) for i in array]

    
    
    for i in range(x):
    
        try:
            aux=array[i+1]
            if array[i]+0==array[i+1] or array[i]+array[i+1]==array[i+2]:
                array[i+1]=array[i+2]
                array[i+2]=aux
            
        except:
            pass
    if array==comprobador and comprobador[1]+0!=comprobador[2]:
        print("NO")
    else:
        print("YES")
        print(array)
"""
"""
#A. Ultra-Fast Mathematician
num1=input()
num2=input()
ans=[]
for i in range(len(num1)):
    
        if num1[i]!=num2[i]:
            ans.append("1")
        else:
            ans.append("0")
    
print("".join(ans))
"""
"""
#Esta bien el codigo pero se demora mucho en el caso #7
magnetismo=int(input())
c=1
previ=int(input())
for i in range(1,magnetismo):
    s=input()
    if previ!=s:
        previ=s
        c+=1
print(c)
"""
"""
t=int(input())
while t>0:

    num=input()
    long=len(num)
    nega_num=-1
    longitud=6

    for i in range(long):
        try:
            if num[0][i]!=num[nega_num]:
                long-=2  
                
        except:
            pass
        nega_num-=1
    print(long) 
"""

