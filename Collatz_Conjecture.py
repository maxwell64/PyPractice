#Runs the Collatz conjecture algorithm to reduce a given number to 1

def Collatz():

  counter = 0

  n = int(input('What is the starting number? '))

  if n < 2:

    print('That doesn\'t work! Try again.')

    n = int(input('Give me a number greater than 1: '))

  while n > 1:

    if n % 2 == 0:

      n = n/2

      counter += 1

      print(n)
    
    else:

      n = ((n*3)+1)

      counter += 1

      print(n)
  
  print('Done! it took %s steps' % counter)

Collatz()
