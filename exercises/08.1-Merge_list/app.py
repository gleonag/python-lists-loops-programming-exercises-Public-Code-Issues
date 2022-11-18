chunk_one = [ 'Lebron', 'Aaliyah', 'Diamond', 'Dominique', 'Aliyah', 'Jazmin', 'Darnell' ]
chunk_two = [ 'Lucas' , 'Jake','Scott','Amy', 'Molly','Hannah','Lucas']


def merge_list(list1, list2):
    #Your code go here:
    merge_list = []
    for array1 in chunk_one:
        merge_list.append(array1)
    for array2 in chunk_two:
        merge_list.append(array2)   
    return merge_list
    
print(merge_list(chunk_one, chunk_two))
