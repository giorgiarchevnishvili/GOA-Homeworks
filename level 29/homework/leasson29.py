def get_even_index_elements(lst):
    return lst[::2] 
    
numbers = [10, 20, 30, 40, 50, 60, 70, 80]
even_index_elements = get_even_index_elements(numbers)
print(even_index_elements)
    






games = ["Minecraft", "Far Cry 5", "Need For Speed", "Mad Max", "Call of Duty"]
programming_languages = ["Python", "JavaScript", "Java", "Html", "Css"]
games = programming_languages
print(games) 


def greet_user(name):
    print(f"Hello, {name}!")
greet_user("Alice")
