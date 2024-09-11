def simple_calculator(num1, num2):
    results = {}

    results['addition'] = num1 + num2
    
    results['subtraction'] = num1 - num2
    
    results['multiplication'] = num1 * num2
    
    if num2 != 0:
        results['division'] = num1 / num2
    else:
        results['division'] = 'Error: Division by zero'
    
    return results



