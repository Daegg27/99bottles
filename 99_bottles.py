def bottle_song(num):

	number_of_beers = num
	
	while number_of_beers > 0:
		if number_of_beers > 2:
			#print(number_of_beers + " bottles of beer on the wall, " + number_of_beers + " bottles of beer")
			print(f"{number_of_beers} bottles of beer on the wall, {number_of_beers} bottles of beer")
			print(f"Take one down and pass it around, {number_of_beers - 1} bottles of beer on the wall")
			#print("Take one down and pass it around, " + (number_of_beers - 1) + " bottles of beer on the wall")

			number_of_beers -= 1
		elif number_of_beers == 1:
			# print(number_of_beers + " bottle of beer on the wall, " + number_of_beers + " bottle of beer")
			print(f"{number_of_beers} bottle of beer on the wall, {number_of_beers} bottle of beer")
			print(f"Take on down and pass it around, no more bottles of beer on the wall")
			# print("Take one down and pass it around, no more bottles of beer on the wall")
		
			number_of_beers -= 1
		else:
			# print(number_of_beers + " bottles of beer on the wall, " + number_of_beers + " bottles of beer")
			print(f"{number_of_beers} bottles of beer on the wall, {number_of_beers} bottles of beer")
			print(f"Take one down and pass it around, {number_of_beers - 1} bottle of beer on the wall")
			# print("Take one down and pass it around, " + (number_of_beers - 1) + " bottle of beer on the wall")
			
			number_of_beers -= 1


bottle_song(42)