#Takes an integer input and converts it to binary or vice versa

def binaryConverter():

  start = str(input('Do you want Binary or Decimal? '))
  start=start.lower()
  
  if start[0] == 'b':
    
    initial = int(input('What is the decimal number? '))
    final = []
    finalBinary = 'The number in binary is: '

    while initial>=1:
      final.append(int(initial%2))
      initial = initial/2
    
    for i in final[::-1]:
      finalBinary += str(i)
    
    print(finalBinary)


  elif start[0] == 'd':
    
    initial = str(input('What is the binary number? '))
    c = 0
    product = 0
    
    for i in initial[::-1]:
      product += int(i) * (pow(2,c))
      c+=1
      
    print(product)


  else:
    print('Peace was never an option!')

binaryConverter()
