import random

num_of_char=int(input("how many char?\n"))
num_of_simbol=int(input("how many simbol?\n"))
num_of_number=int(input("how many namber?\n"))
sum=num_of_char+num_of_number+num_of_simbol
passwordlist=[]
list_of_simbol=['@','#','&','*','%','!','$','^']
for i in range(0,num_of_char):
    a =random.randint(97,122)
    b=random.randint(65,90)
    t=random.choice([a,b])
    passwordlist.append(chr(t))
for i in range(0,num_of_number):
    a=random.randint(0,9)
    passwordlist.append(a)
for i in range(0,num_of_simbol):
    a=random.randint(0,len(list_of_simbol)-1)
    passwordlist.append(list_of_simbol[a])

random.shuffle(passwordlist)

print(''.join(str(e) for e in passwordlist))
