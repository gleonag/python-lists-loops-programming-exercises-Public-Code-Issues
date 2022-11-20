Celsius_values = [-2,34,56,-10]



def fahrenheit_values(x):
# the magic go here:
    return (x * 9 / 5) + 32
   
result = map(fahrenheit_values, Celsius_values)
print(list(result))
