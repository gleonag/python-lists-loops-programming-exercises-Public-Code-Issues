parking_state = [
  [1,1,1],
  [0,0,0],
  [1,1,2]
]

#Your code go here:

def get_parking_lot(matriz):
  state = {'occupied_slots':0, 'available_slots':0,'total_slots':0}
  for i in range(len(matriz)):
    for k in range(len(matriz[i])):
      if matriz[i][k]==1:
        state['occupied_slots'] +=1
        state['total_slots'] += 1
      elif matriz[i][k]==2:
        state['available_slots'] +=1
        state['total_slots'] +=1
  return state

print (get_parking_lot(parking_state))

