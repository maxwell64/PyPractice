#Converts a given string into pig latin

def Pig_Latin(thing):

  thing = thing.lower()

  thing += thing[0]

  thing = thing[1::]

  thing += 'ay'

  print(thing)
    
  
test = 'Jeff'

Pig_Latin(test)
