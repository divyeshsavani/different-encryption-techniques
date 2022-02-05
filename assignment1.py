import random
import time
from Crypto.Cipher import AES
import os

# millerRabin function
def millerRabin(n,s,d,i):
    a = random.randrange(2, n)
    print("\na is", a)
    x = pow(a,d) % n
    print("This is round",i,"and x = ",x)
    if(x==1 or x==(n-1)):
        # print("true",i)
        return True
    else:
        # print("in else")
        for p in range(0,s-1):
            x=(x*x)%n
        if(x==(n-1)):
            # print("true",i)
            return True
        else:
            # print("false",i)
            return False
    # return True

# find GCD of two number
def calGcd(p,q):
    if q==0:
        return p
    else:
        return calGcd(q, p%q)

# Chinese Remainder Theorem
def findXCrt(num,rem):
    x=1
    timeStart = time.time() + 10
    # print("in crt function")
    while(time.time() < timeStart):
        count=0
        while(count<3):
            if(x%num[count] != rem[count]):
                break
            count += 1
        if(count == 3):
            return x
        x += 1
    return 0  

# AES Encrption and Decryption]

def aes(text):
    text = text.encode("utf8")
    # Generating a Key
    key = os.urandom(16)
    # Initialization Vector
    iv = os.urandom(16)
    print("\n \t key for encrption : ",key)
    # Encrypting with AES
    enc = AES.new(key, AES.MODE_CBC, iv)
    ciphertext = enc.encrypt(text)
    print("\n \t Encrpyted message : ",ciphertext)
    # Decrypting with AES
    dec = AES.new(key, AES.MODE_CBC, iv)
    plainText = dec.decrypt(ciphertext)
    print("\n \t Decrypted message :", plainText)

# MAIN MENU
print("\n4Welcome to an Assignment 1: Codes, Number Theory, and Symmetric Encryption Cryptography and Secure Communications (MITS5500/CSCI5310)")

while True:   
    print("\n1. Primality Test using Miller-Rabin")  
    print("2. Chinese Reminder Theorem")
    print("3. Symmetric Encryption")  
    print("4. Exit")  
    choice = int(input("\nEnter the Choice:"))  
    
    # Miller-Rabin Algorithm
    if choice == 1:  
        number1 = int(input("\nEnter the number which you want to be tested for primality (less than 10,000):"))
        if number1 in (0,1):
            print("\n\t", number1 , "is neither prime or composite")
        elif number1 in (2,3):
            print("\n\t", number1 , "is prime")
        elif number1>10000:
            print("\n Enter number less than 10,000")
        elif number1 % 2 == 0 :
            print("\n\t", number1 , "is composite")
        else:
            round = int(input("\nEnter the number of rounds of testing to perform:"))
            s=count=0
            d=number1-1
            # find s and d(odd) so that (2^s)*d = (number1)-1
            while d%2==0:
                d>>=1
                s+=1
            print ("(d,s) : ",d,s)
            # calling function for round times
            for i in range(0,round):
                if(millerRabin(number1,s,d,i) == False):
                    count=count+1   
            if(count<round):
                print("\n\n\t", number1, "is prime\n")
            else:
                print("\n\n\t", number1, "is composite\n")
    # Chinese Reminder Theorem
    elif choice == 2:  
        print("\nEnter Three Number which is coprime\n")
        relPrime = []
        for i in range(0,3):
            relPrime.append(int(input("Enter the number : ")))
        # print(relPrime) 

        #check wheather input numbers are relatively prime or not 
        if(calGcd(relPrime[0],relPrime[1]) == calGcd(relPrime[1],relPrime[2]) == calGcd(relPrime[0],relPrime[2]) == 1):
            rem = []
            for i in range(0,3):
                rem.append(int(input("Enter the reminder : ")))
            x = findXCrt(relPrime,rem)
            if(x==0):
                print("\n\t X is not feasible")
            else:
                print ("\n\t X, using Chinese Remainder Theorem, is : ", x,"\n")
        else:
            print("\n\tGiven numbers are not coprime\n")
    
            
    # Symmetric Encryption
    elif choice == 3:  
        text = input("\nEnter the 16 letter message(including space) you want to encrypt : ")
        if(len(text) == 16):
            aes(text)
        else:
            print("\n\tPlease enter 16 letter message")
        
    elif choice == 4:  
        break  
    
    else :
        print("\n\tEnter valid choice\n")
