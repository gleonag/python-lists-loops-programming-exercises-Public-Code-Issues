#Remember import random function here:
import random

my_list = [4,5,734,43,45]

#The magic is here:
for i in range(0,10):
    i = random.randint(0, 1000)
    print(i)

out_arr = np.add(my_list,i)
print(out_arr)