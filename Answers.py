import pickle
import csv
class Question1():
    def create():
        fh=open('text.txt','w')
        string="""Neither apple nor pine are in pineapple. Boxing rings 
are square.  
Writers write, but fingers don’t fing. Overlook and 
oversee are opposites.  
A house can burn up as it burns down. An alarm goes 
off by going on."""
        for i in string.split('\n'):
            fh.write(i)
        fh.close()

    def partA():
        fh=open('text.txt','r')
        string=fh.read()
        print(string)
        fh.close()

    def partB():
        string="Cargo goes by ship and shipment goes by car"
        fh=open('text.txt','a')
        fh.write(string)
        fh.close()
        fh=open('text.txt','r')
        string=fh.readline()
        for i in range(len(string.split("."))):
            if i != len(string.split(".")):
                print("{}: {}.".format((i+1),(string.split('.')[i]).strip()))
        fh.close()

    def partC():
        fh=open("text.txt",'r')
        string=fh.read()
        print('{}.'.format((string.split('.')[-2]).strip()))
        fh.close()
    
    def partD():
        fh=open("text.txt",'r')
        string=fh.read()
        print('{}.'.format(((string.split('.')[0]).strip())[10:]))
        fh.close()

    def partE():
        fh=open("text.txt",'r')
        string=fh.read()
        count=int(input("Enter the line number: "))
        print('{}.'.format((string.split('.')[count-1]).strip()))
        fh.close()

    def partF():
        fh=open("text.txt",'r')
        L=(fh.read()).split()
        D={}
        for i in L:
            if len(i) not in('A','An','The'):
                if i[0].lower() in D or i[0].upper() in D:
                    D[i[0].lower()]+=1
                else:
                    D[i[0].lower()]=1
        for i in D:
            print('Words beginning with {}: {}'.format(i,D[i]))
        fh.close()
        
class Question2():
    def isvowel ():
        vowels=['a','e','i','o','u']
        fh=open('file1.txt')
        L=(fh.read()).split()
        fh.close()
        fh=open('file2.txt','w')
        for i in L:
            if i[0].lower() not in vowels:
                fh.writelines(i+'\n')
        fh.close()

class Question3():
    def Answer():
        fh=open('text.txt')
        L1=fh.readlines()
        L2=[]
        for i in L1:
            L2.append(tuple(i))
        print(L2)
        fh.close()

class Question4():
    def Answer():
        fh=open("myfile.txt")
        L=(fh.read()).split()
        D={}
        for i in L:
            if i.lower() in D or i[0].upper() in D:
                D[i.lower()]+=1
            else:
                D[i.lower()]=1
        print(D)
        fh.close()

class Question5():
    def Answer():
        #import pickle first
        Customer={'roomno':10,'name':'Adith','duration(days)':3}
        fh=open('hotel.dat','wb')
        pickle.dump(Customer,fh)

class Question6():
    def Answer():
        f=open('placement.csv','w') 
        w=csv.writer(f) 
        w.writerows([['s.no','name','marks1','marks2','marks3', 'marks4','marks5'], 
                [1,'John', 4, 3, 4, 2, 5], 
                [2,'Peter', 3, 4, 4, 3, 5]]) 
        f.close()

class Question7():
    def count(n):
        return len(n)
    
    def reverse(n):
        return n[::-1]

    def hasdigit(n):
        condition=False
        for i in list(n):
            if i.isdigit():
                condition=True
        return condition
    
class Question8():
    class perfect():
        def perfectnum(n):
            sum=0
            for i in range(1,n):
                if n%i==0:
                    sum+=i
                else:
                    pass
            if sum==n:
                return True
            else:
                return False
        def main():
            continuee=True
            while continuee==True:
                choice=int(input("Main Menu\n1) Run The Program\n2)Exit"))
                if choice==2:
                    continuee=False
                    break
                n=int(input("Enter a Number: "))
                print(Question8.perfect.perfectnum(n))

class Question9():
    def romanToInt(s):
        Roman=str(s)
        Decimal=0
        D1={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        D2={'CM':900,'CD':400,'XC':90,'XL':40,'IX':9,'IV':4}
        try:
            while True:
                if Roman[0:2] in D2:
                    Decimal+=D2[Roman[0:2]]
                    Roman=Roman[2:]
                else:
                    Decimal+=D1[Roman[0]]
                    Roman=Roman[1:]
        except:
            print(Roman)
            if Roman in D1:
                Decimal+=D1[Roman]
            return Decimal

class Question10():
    def Answer(n):
        #Take input for n as a string
        Type=None
        for i in list(n):
            if i in [0,1]:
                if Type==None:
                    Type='B'
                if i in [2,3,4,5,6,7]:
                    if Type=='B':
                        Type='O'
                    if i in [8,9,'A','B','C','D','E','F']:
                        Type='H'
        return Type