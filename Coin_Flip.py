#simulates flipping a coin a desired number of times and returns the results

import random

def coinflip():

  heads = 0
  tails = 0

  tries = input('How many times? ')

  tries = int(tries)

  for i in range(tries):

    result = random.randint(0,1)

    if result == 0:

      tails += 1
    
    else:
      heads += 1
  
  print('You got %s heads and %s tails.' %(heads,tails))

coinflip() 
