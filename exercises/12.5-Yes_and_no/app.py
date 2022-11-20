theBools = [0,1,0,0,1,1,1,0,0,1,0,1,1,0,0,0,0,0,0,0,0,1,0,0,0,0,1]

#Your code go here:

def wokis(num):
    if num == 0:
        return('woko')
    else:
        return('wiki')
    
   
newList = map(wokis,theBools)
print(list(newList))

