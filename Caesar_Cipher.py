#Takes a string input and then enciphers it using a given key and a casar cipher

def Caesar():

  inp_list = []
  outp_list = []

  inp = str(input('What would you like enciphered? '))

  key = int(input('What is your key? '))
  
  alph = 'abcdefghijklmnopqrstuvwxyz'

  for x in inp:

    inp_list.append(x)
  
  for y in inp_list:

    y_pos = alph.find(y)

    outp_list.append(alph[y_pos + key])

    

  outp = ''

  for z in outp_list:
    outp += z

  print(outp)

Caesar()
