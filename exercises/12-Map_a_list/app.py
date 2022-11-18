Celsius_values = [-2,34,56,-10]



def fahrenheit_values(x):
# the magic go here:
    return Celsius_values * 33,8
   
result = list(map(fahrenheit_values))
print(result)



# numbers1 = [1, 2, 3]
# numbers2 = [4, 5, 6]
  
# result = map(lambda x, y: x + y, numbers1, numbers2)
# print(list(result))