# CPW 101 Programming Assignment 7
# This file contains starter code for the following:

# Modify a previous program so that the user
# can use its code as many times as they wish.

CENTS_PER_QUARTER = 25 # a quarter is 25 cents
CENTS_PER_DIME = 10    # a dime is 10 cents
CENTS_PER_NICKEL = 5   # a nickel is 5 cents
CENTS_PER_PENNIES = 1 
# The original program calculated the value of some coins.

while True:
      
           
      # get input
      print('We will convert coins to cents.')
      quarters = int(input('How many quarters? '))
      if quarters < 0:
            break
      dimes = int(input('How many dimes? '))
      if dimes < 0:
                  break
      nickels = int(input('How many nickels? '))
      if nickels < 0:
                  break
      pennies = int(input('How many pennies? '))
      if pennies < 0:
            break
      # process the input,
      # calculate the total value, in cents,
      # of the coins input by the user.
      cents = CENTS_PER_QUARTER * quarters \
            + CENTS_PER_DIME * dimes \
            + CENTS_PER_NICKEL * nickels \
            + CENTS_PER_PENNIES * pennies \

      # display the original coin quantities
      # and the calculated value.
      print( quarters, 'quarters',
            dimes, 'dimes',
            nickels, 'nickels',
            pennies, 'pennies',
            'is', cents, 'cents.')

      if True:
            choice = input(f"Do you want to convert more coins?,(y/yes):").lower().strip()
                  
            if choice not in ["y","yes"]:
           
                  break

           
        
             

                  
                  
           
      
      