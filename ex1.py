import re

def find(mot, para):
     f= re.findall(mot, para, flags=re.IGNORECASE)
     list=[]
     if f !=  []:
          return True
     else:
          return  False
     

para=str(input("enter a paragraph: "))
mot=str(input("enter the word to be searched: "))
r=find(mot,para)
if r == True:
    print("the word exist in the  paragraph")
else:
     print("sorry!the word dosn't exist")

