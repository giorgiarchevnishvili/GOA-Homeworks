#ააგეთ პროგრამა, რომელიც მოსთხოვს მომხმარებელს, რომ შეიყვანეს რიცხვი 1 - 100 მდე.პროგრამის დანიშნულება არის ის, რომგამოიცნოს მომხმარებლის მიერ შემოტანილი რიცხვი, იმდენჯერ მიეცეს გამოცნობის შესაძლებლობა სანამ საბოლოოდ არ გამოიცნობს. 
import random

print("Enter the number 1 to 100 :")
user_number = int(input())

attempts = 0

while True:

    guess = random.randint(1, 100)
    attempts += 1
    
    if guess < user_number:
        print(f"{guess} Less, try again.")
    elif guess > user_number:
        print(f"{guess} There are more, try again.")
    else:
        print(f"Congratulations! {guess} That's right! I guess {attempts} On the step ")
        break


## 3) დავალება
 #'FizzBuzz' 
#FizzBuzz მიზანი:
# შექმენით პროგრამა, რომელიც ბეჭდავს რიცხვებს 1-დან 100-მდე. თუმცა 3-ის ჯერადებისთვის რიცხვის ნაცვლად დაბეჭდეთ „Fizz“, ხოლო 5-ის ჯერადებისთვის დაბეჭდეთ „Buzz“. 3-ისა და 5-ის ჯერადი რიცხვებისთვის დაბეჭდეთ "FizzBuzz".  მოთხოვნები: გამოიყენეთ მარყუჟი 1-დან 100-მდე რიცხვების გასამეორებლად.
#გამოიყენეთ პირობითი განცხადებები, რათა შეამოწმოთ რიცხვი იყოფა 3-ზე, 5-ზე ან ორივეზე. დაბეჭდეთ შესაბამისი სიტყვა ("Fizz", "Buzz" ან "FizzBuzz") ან ნომერი.

for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)

## 4 დავალება
#დაწერეთ პროგრამა სადაც შეამოწმეთ, სტუდენტმა ჩააბარა თუ არა ჩააბარა კურსი მათი გამოცდის ქულების მიხედვით. სთხოვეთ მომხმარებელს შეიყვანოს ქულები შუალედური გამოცდისთვის, დასკვნითი გამოცდისთვის და პროექტისთვის. დარწმუნდით, რომ მომხმარებელმა შეიყვანოს სწორი ქულები (პოზიტიური რიცხვები 0-დან 100-მდე) თითოეული კომპონენტისთვის.
#გამოიყენეთ შემდეგი შეფასების კრიტერიუმები: თუ საშუალო ქულა (20% შუალედური კურსისთვის, 40% საბოლოო და 40% პროექტისთვის) არის 70 ან მეტი, სტუდენტი გაივლის კურსს. თუ საშუალო ქულა 70-ზე დაბალია, სტუდენტი ვერ ახერხებს კურსის ჩაბარებას. აჩვენეთ მომხმარებლისთვის შეტყობინება, რომელშიც მითითებულია მისი გავლის/ჩავარდნის სტატუსი და გამოთვლილი საშუალო ქულა.


def get_valid_score(prompt):
    while True:
        try:
            score = float(input(prompt))
            if 0 <= score <= 100:
                return score
            else:
                print("Invalid score! Please enter a number between 0 and 100.")
        except ValueError:
            print("Invalid input! Please enter a numeric value.")

def main():
    midterm_score = get_valid_score("Enter the midterm exam score (0-100): ")
    final_score = get_valid_score("Enter the final exam score (0-100): ")
    project_score = get_valid_score("Enter the project score (0-100): ")
    
    average_score = (midterm_score) + (final_score) + (project_score) /3
    
    if average_score >= 50:
        status = "passed"
    else:
        status = "failed"
    
    print(f"Pass/Fail Status: {status}")
    print(f"Calculated Average Score: {average_score:.2f}")

if __name__ == "__main__":
    main()




#დაწერეთ პროგრამა სადაც შეამოწმებთ, აქვს თუ არა ადამიანს მართვის მოწმობის აღების უფლება მისი ასაკისა და მართვის გამოცდილებიდან გამომდინარე. დარწმუნდით, რომ მომხმარებელი შეიყვანს თავისი ასაკს და წლების რაოდენობა, რომელსაც მანქანას მართავდა.მომხმარებელმა უნდა შეიყვანოს დადებითი მთელი რიცხვები ასაკისა და მართვის გამოცდილებისთვის. (დაგნა მოხდეს ოპერაციები)
#გამოიყენეთ შემდეგი საკვალიფიკაციო კრიტერიუმები: პირი უნდა იყოს მინიმუმ 18 წლის მართვის მოწმობის მისაღებად. თუ პირი 18 წლამდეა, მას არ შეეძლება მართვის მოწმობის აღება. თუ პირი არის 18 წლის ან მეტი, მას უნდა ჰქონდეს მინიმუმ 1 წლიანი მართვის გამოცდილება, რომ დაშვებული იყოს მართვის მოწმობის აღებისთვის.
#მომხმარებლისთვის აჩვენეთ შეტყობინება, რომელშიც მითითებულია მართვის მოწმობის მიღების უფლება

age = int(input("enter your age: "))
experince_in_drive = int(input("enter ride experience: "))

if age < 18:
   print("you cant take drive license")
elif age >= 18 and experince_in_drive >= 2:
   print("you cant take drive license")










































