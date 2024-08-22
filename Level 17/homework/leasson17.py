# 1)for loop-ის საშუალებით ტერმინალში გამოიტანეთ 30-ჯერ "GOA IS THE BEST"
for i in range(30):
    print("GOA IS THE BEST")
 
 #2)for loop-ის საშუალებით ტერმინალში 5-დან 150-ის ჩათვლით ნომრები
for i in range(5 , 151):
    print(i)

 # 3)for loop-ის საშუალებით ტერმინალში გამოიტანეთ 2-დან 50-ის ჩათვლით ნომრები ოღონდ ნაბიჯი იყოს 4 ანუ ყოველ i-ს თითეულ ნაბიჯზე დაემატოს 4
for i in range(2, 51, 4):
    print(i)

#4) for loop-ის საშუალებით ტერმინალში გამოიტანეთ  10-ჯერ ყოველი ( i ელემენტი და გვერდით მიუწერეთ, "GOA") i --------- საიტერაციო ცვლადი
for i in range(1, 11):
    print(f"{i} - GOA")

# 5) დაწერეთ პროგრამა for loop-ის გამოყენებით, რომელიც გამოგვიტანს ჯერ ლუწს და შემდეგ კენტს.

for i in range(1, 21):
    if i % 2 == 0:
        print(f"{i} - Evenness")


for i in range(1, 21):
    if i % 2 != 0:
        print(f"{i} - Kent")

#6) შექმენით პროგრამა სადაც გამოიყენებთ While loop - ს. თქვენი დავალება იქნება ის, რომ მომხამრებელს შემოატანინოთ რიცხვი და თქვენ უნდა გამოიცნოთ ეს რიცხვი, ხოლო ყოველ არ გამოცნობილ რიცხვზე ისევ თავიდან უნდა შეგეკითხოთ და შეიყვანოთ რიცხვი.
import random


secret_number = random.randint(1, 100)

while True:

    user_input = input("Enter the number 1 to 100: ")
    
  
    try:
        guessed_number = int(user_input)
    except ValueError:
        print("Please enter the correct number.")
        continue

   
    if guessed_number == secret_number:
        print("Congratulations! You guessed the number.")
        break
    else:
        print("Incorrect guessing. Try again.")
