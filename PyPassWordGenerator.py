#Easy Case:
import random
letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p',
           'q','r','s','t','u','v','x','y','z','A','B','C','D','E','F','G',
           'H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','X',
           'Y','Z']
numbers = ['0','1','2','3','4','5','6','7','8','9']
symbols = ['!','#','$','%',' &','(',')','*','+']

''''print("Welcome to Pypassword generator!")
nr_letters = int(input("How many letters would you like in your Password: "))
if nr_letters<4:
    print('Less than 4 is not safe please re-enter \n')
    nr_letters = int(input("How many letters would you like in your Password: "))

nr_symbols = int(input("How many symbols would you like: "))
nr_numbers = int(input("How many numbers would you like: "))
   
n_l = nr_letters - (nr_symbols+nr_numbers)
s =''
for p in range(0,n_l):
    s+=random.choice(letters)
for sy in range(0,nr_symbols):
    s+=random.choice(symbols)
for nu in range(0,nr_numbers):
    s+=random.choice(numbers)

print(s)'''

# Hard Case
print("Welcome to Pypassword generator!")
nr_letters = int(input("How many letters would you like in your Password: "))
if nr_letters<4:
    print('Less than 4 is not safe please re-enter \n')
    nr_letters = int(input("How many letters would you like in your Password: "))

nr_symbols = int(input("How many symbols would you like: "))
nr_numbers = int(input("How many numbers would you like: "))
   
n_l = nr_letters - (nr_symbols+nr_numbers)
s =[]
for p in range(0,n_l):
    s.append(random.choice(letters))
for sy in range(0,nr_symbols):
    s+=random.choice(symbols)
for nu in range(0,nr_numbers):
    s+=random.choice(numbers)
    
random.shuffle(s)
password=''
for char in s:
    password+=char
print(password)
