import math

myAge = int(input("Type your age: "))

if myAge >= (122):
		print("Your about to die")
elif myAge >= (17):
		print("You can watch R Rated Movies")
elif myAge >= (13):
		print("You can watch PG-13 Rated Movies")
elif myAge >= (1):
		print("You can watch G Rated Movies")
elif myAge <= (0):
		print("No movies, your a fetus!")
else:
		print("That's not a proper age!")