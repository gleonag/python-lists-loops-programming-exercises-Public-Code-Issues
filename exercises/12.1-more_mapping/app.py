myNumbers = [23,234,345,4356234,243,43,56,2]

#Your code go here:

def increment_by_one(numero):
    return numero * 3

new_list = map(increment_by_one, myNumbers)
print(list(new_list))
