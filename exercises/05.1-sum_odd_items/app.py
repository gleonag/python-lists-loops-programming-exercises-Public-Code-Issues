arr = [4,5,734,43,45,100,4,56,23,67,23,58,45]

#Your code go here:
 
    
def sum_odds(items):
    odd_list = []
    for numb in arr:
        if numb % 2 != 0:
            odd_list.append(numb) 
    return sum(odd_list)

print(sum_odds(arr))



