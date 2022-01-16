#RSA Algorithm

import random as r

#check whether prime or not
def isPrime(x):
    for i in range(2,x//2+1):
        if x%i==0:
            return False
    return True

#to find prime in the given range
def randomPrime(a,b):
    for i in range(a,b):
        if isPrime(i):
            return i
        
#Eculid division method to find public key        
def gcd(x,y):
    if x<y:
        x,y=y,x
    while y!=0:
        temp=x
        x=y
        y=temp%x
    return x

#generating two large random prime numbers p and q
p=randomPrime(r.randint(100, 500),r.randint(501, 1000))
q=randomPrime(r.randint(100, 500),r.randint(501, 1000))
if p==q:
    while p!=q:
        q=randomPrime(r.randint(100, 500),r.randint(500, 1000))
print(p,q)

#finding n and phi
n=p*q
phi=(p-1)*(q-1)
print(n,phi)

#public key
for i in range(2,phi):
    if gcd(i,phi)==1:
        e=i
        break

#private key
for i in range(2,phi):
    if ((e*i)-1)%phi==0:
        d=i
        break
    
print("Public key & Private key:",e,d)

msg=input("Enter the msg to be encrypted: ")

#converting the msg into equivalent integer value
num=[]
for i in msg:
    num.append(ord(i))

#encryption process
#generating cipher text using public key
c=[]
ct=[]
for i in num:
    c.append((i**e)%n)
    ct.append(chr((i**e)%n))

print("\nCipher numbers:")
for i in c:
    print(i,end=" ")

print("\n\nCipher text:")
for i in ct:
    print(i,end="")
  

#decryption process
#generating plain text using private key
print("\n\nDecrypted message: ")
for i in c:
    x=(i**d)%n
    print(chr(x),end="")
