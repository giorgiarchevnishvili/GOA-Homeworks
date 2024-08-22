#შექმენით სია და შეიტანეთ 10 სხვადასხვა მონაცემთა ტიპის მნიშვნელობა, შემდეგ 5 მონაცემს  შეუცვალეთ   მნიშვნელობა და შემდეგ დაპრინტეთ მთლიანი სია.
data_list = [
      41,                 # int
     3.19,               # float
     "Hello, World!",    # str
     True,               # boolean
     [1, 2, 4],          # list
]

data_list[0]= 200
data_list[1]= 4.16
data_list[2]= "Hello Chads"

print(data_list)

#3) სიაში ელემენტების ჯამი
#შექმენი სია, რომელიც შეიცავს რიცხვებს. დაწერე კოდი, რომელიც გამოითვლის ამ სიის ელემენტების ჯამს და დაბეჭდავს შედეგ
numbers = [10, 20, 2003, 40, 100]

total_sum = sum(numbers)

print("all_numb:", total_sum)

#4) სიის ყველა ელემენტის გაორმაგება
#შექმენი სია რიცხვებით. დაწერე კოდი, რომელიც თითოეული ელემენტის გაორმაგებულ მნიშვნელობას შეიცავს ახალ სიაში და დაბეჭდავს მას.
numbers = [1, 2, 3, 4, 5]

doubled_numbers = [x * 2 for x in numbers]

print("doubled:", doubled_numbers)

numbers = [1, 2, 3, 4, 5]

doubled_numbers = list(map(lambda x: x * 2, numbers))

print("doubled:", doubled_numbers)


#5) სიის ელემენტების გამრავლება
#შექმენი სია რიცხვებით და დაწერე კოდი, რომელიც გამოითვლის სიის ყველა ელემენტის ნამრავლს და დაბეჭდავს შედეგს.

import math

numbers = [2, 3, 4, 5]

product = math.prod(numbers)

print("sum:", product)

from functools import reduce
import operator

numbers = [2, 3, 4, 5]

product = reduce(operator.mul, numbers, 1)

print("elements:", product)
