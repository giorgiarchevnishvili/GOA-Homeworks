def simple_calculator(x, y):
    results = {}
    
    results['addition'] = x + y
    
    results['subtraction'] = x - y
    
    results['multiplication'] = x * y
    
    if y != 0:
        results['integer_division'] = x // y
    else:
        results['integer_division'] = 'Error: Division by zero'
    
    return results

x = 10
y = 3
print(simple_calculator(x, y))




def user(name):
    greeting = f"hello {name}, Welcome to the Teahouse, I wish you good luck and moving forward"
    print(greeting)


def love_letter(name):
    letter = (
        f"dear {name},nn"
        "Your heartfelt support and warmth make our relationship special. "
        "Every day is a joy for me when I think you exist in my life. "
        f"{name}"
    )
    print(letter)

love_letter ("Nini")
