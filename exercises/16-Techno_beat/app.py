

# Your code go above, nothing to change after this line:
print(lyrics_generator([0,0,1,1,0,0,0]))
print(lyrics_generator([0,0,1,1,1,0,0,0]))
print(lyrics_generator([0,0,0]))
print(lyrics_generator([1,0,1]))
print(lyrics_generator([1,1,1]))



def lyrics_generator(lista):
   ritmo = {'Boom' : 0, 'Drop the base':0 , '!!!Break the base!!!':0}
   for i in range(len(lista)):
    if lista(i) == 0:
        ritmo['Boom'] += 1
        
    elif lista(i) == 1:
        ritmo['Drop the base'] += 1
        ritmo['!!!Break the base!!!']+=1

    return ritmo



# def get_parking_lot(matriz):
#   state = {'occupied_slots':0, 'available_slots':0,'total_slots':0}
#   for i in range(len(matriz)):
#     for k in range(len(matriz[i])):
#       if matriz[i][k]==1:
#         state['occupied_slots'] +=1
#         state['total_slots'] += 1
#       elif matriz[i][k]==2:
#         state['available_slots'] +=1
#         state['total_slots'] +=1
#   return state

# print (get_parking_lot(parking_state))