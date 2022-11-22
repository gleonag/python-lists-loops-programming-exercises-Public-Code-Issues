list_of_numbers = [4,	80,	85,	59,	37, 25, 5, 64, 66, 81, 20, 64, 41, 22, 76, 76, 55, 96, 2, 68]


#Your code here:
def merge_two_list(list_of_numbers):
    odd = []
    even = []
    for numb in list_of_numbers:
        if numb % 2 == 0:
            even.append(numb)
            # print(even)
        else:
            odd.append(numb)
            # print(odd)
    return [odd] + [even]
print(merge_two_list(list_of_numbers))

# mismo resultado!!