#1) input
#პირველი დავალება --- 
#მომხმარებელმა უნდა შემოიტანოს რიცხვი 1 - დან 1000 - მდე, თქვენი მიზანია, რომ გამოიცნოთ შემოტანილი რიცხვი, თუ სწორი იქნება დაპრინტეთ 'სწორია!', ხოლო თუ არასწორია, დაპრინტეთ ;არასწორია!'
number = int(input("enter a number from 1 to 1000: "))
guess_number = 10
is_equal = number == guess_number
print("ur final answer is correct", is_equal)



#მეორე დავალება ---

#დაწერეთ პროგრამა, რომელიც მოუწოდებს მომხმარებელს შეიყვანოს ნივთების რაოდენობა, რომლის შეძენაც სურს.
#დარწმუნდით, რომ მომხმარებელი შეიყვანს დადებითი რიცხვს.
#თითოეული ნივთისთვის, შესთავაზეთ მომხმარებელს შეიყვანოს ფასი.
#დარწმუნდით, რომ მომხმარებელი შეიყვანოს დადებითი რიცხვს პროდუქტის ფასისთვის.
#გამოთვალეთ და აჩვენეთ ყველა ელემენტის მთლიანი ღირებულება.

item = int(input("enter item that you like: "))
price = int(input("enter item's price: "))




#გააკეთეთ 10 მაგალითი შედარებით ოპერატორებზე.
print(10 > 10 and 11 <22)
print(11 < 10 and 1 < 2)
print(100 > 10 and 89 > 87)
print(178 < 179 and 18765 > 1)
print(16 > 17 and 189 > 5)
print(19 > 22 or 1 > 2)
print(67 > 66 or 44 < 3)
print(7 > 7 or 5 < 5)
print(555 > 67 or 88 < 8)
print(22 < 0 or 33 < 2)



#3) ლოგიკური ოპერატორები


#პირველი დავალება ---
#დაწერეთ პროგრამა,  რათა შეამოწმოთ, აქვს თუ არა მომხმარებელს ფასდაკლების უფლება მისი ასაკისა და შესყიდვის მთლიანი თანხის მიხედვით. შესთავაზეთ მომხმარებელს შეიყვანოს მათი ასაკი და შესყიდვის მთლიანი თანხა. დარწმუნდით, რომ მომხმარებელი შეიყვანს დადებითი რიცხვს ასაკისა და შესყიდვის თანხისთვის. გამოიყენეთ შემდეგი ფასდაკლების წესები: 60 წელზე უფროსი ასაკის მომხმარებლებს შეუძლიათ ისარგებლონ ფასდაკლებით.
#კლიენტებს, რომლებიც ხარჯავენ $100 ან მეტს, შეუძლიათ მიიღონ ფასდაკლება. 60 წელზე უფროსი ასაკის მომხმარებლები და 100 დოლარი ან მეტი დახარჯული აქვთ უფრო მაღალი ფასდაკლების უფლება. მომხმარებლისთვის აჩვენეთ შეტყობინება, რომელშიც მითითებულია, შეუძლიათ თუ არა მას ფასდაკლება და ფასდაკლების ოდენობა, თუ ეს შესაძლებელია.

def check_discount_eligibility(age, purchase_amount):
    eligible_for_discount = False
    discount_amount = 0
    
    # Check age eligibility
    if age > 60:
        eligible_for_discount = True
        
    # Check purchase amount eligibility
    if purchase_amount >= 100:
        eligible_for_discount = True
        
    # Calculate discount amount if eligible
    if eligible_for_discount:
        discount_amount = 10  # Assume a $10 discount
        
    # Return eligibility and discount amount
    if eligible_for_discount:
        return f"You are eligible for a discount of ${discount_amount}.", discount_amount
    else:
        return "You are not eligible for any discount.", 0

# Input age and purchase amount from the user
age = int(input("Enter your age: "))
purchase_amount = float(input("Enter the purchase amount: "))

# Check eligibility and get discount message
message, discount = check_discount_eligibility(age, purchase_amount)
print(message)



#მეორე დავალება ---

#დაწერეთ პროგრამა, რათა შეამოწმოთ, არის თუ არა სტუდენტი უფლებამოსილი სტიპენდიის მისაღებად მათი აკადემიური მოსწრებისა და ოჯახის შემოსავლის მიხედვით. სთხოვეთ მომხმარებელს შეიყვანოს თავისი GPA (საშუალო ქულა) და ოჯახის შემოსავალი. დარწმუნდით, რომ მომხმარებელი შეიყვანს დადებითრიცხვებს. გამოიყენეთ შემდეგი დასაშვებობის კრიტერიუმები: სტუდენტები GPA 3.
#5 ან მეტი ადამიანი უფლებამოსილია სტიპენდიის მისაღებად. სტუდენტები, რომლებსაც აქვთ GPA 3.0 ან მეტი და ოჯახის შემოსავალი $50,000-ზე ნაკლები, შეუძლიათ მიიღონ უმაღლესი სტიპენდია. სტუდენტები, რომლებსაც აქვთ GPA 3.0-ზე დაბალი, არ შეუძლიათ სტიპენდიის მიღება. მომხმარებლისთვის აჩვენეთ შეტყობინება, რომელშიც მითითებულია, რამდენად შეუძლიათ სტიპენდიის მიღება და სტიპენდიის ოდენობა, თუ ეს შესაძლებელია.


def check_scholarship_eligibility(gpa, family_income):
    if gpa >= 3.5:
        return True, "You are eligible for a scholarship."
    elif gpa >= 3.0 and family_income < 50000:
        return True, "You are eligible for a higher scholarship."
    else:
        return False, "You are not eligible for any scholarship."

# Input GPA and family income from the user
gpa = float(input("Enter your GPA: "))
family_income = float(input("Enter your family income: "))

# Check scholarship eligibility and get message
eligible, message = check_scholarship_eligibility(gpa, family_income)
print(message)

# Additional condition to show scholarship amount if eligible
if eligible:
    if gpa >= 3.5:
        print("Scholarship amount: $5000")
    elif gpa >= 3.0 and family_income < 50000:
        print("Higher scholarship amount: $10000")


#4) მონაცემთა ტიპები


#შემოიტანეთ სხვადასხვა ცვლადები, რომლებსაც ექნებათ სხვადასხვა მონაცემთა ტიპი, შემდგომ შეამოწმეთ ეს ტიპები.

name = "john"
age = 100
last_name = "wayne"

print(f"type of 'name' : {type(name)}")
print(f"type of 'age' : {type(age)}")
print(f"type of 'last_name' : {type(last_name)}")
