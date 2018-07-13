
print ('Here at Tampa Bank, we offer simple interest where' +  
' every year we add 1.1x the initial investment')

"""This chunk asks for the length of time they will keep the money in the bank.
A more complex code will convert the length in days to years or ask for both!"""
year = input('How many years do you want to keep your money for?')
type(year)

"""This is just the principal investment"""
principal = input('How much will your initial investment be? $')
type(principal)

"""This is the final statement to the user using both of their inputs!"""
print('This is how much your inital investment of', principal,  'will be worth in', year, 'years')

final = (float(principal) * (1.1 ** float(year)))
print (round(final,2)) \