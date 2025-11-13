def bottle_song():
	finished_drinking = "No more bottles of beer on the wall, no more bottles of beer."
	empty_drinking = "Go to the store and buy some more, 99 bottles of beer on the wall"
	
	before_drinking_string = (f"{current_num_of_beers} bottle of beer on the wall, {current_num_of_beers} bottles of beer")
	# print(before_drinking_string)
	after_drinking_string = (f"Take one down and pass it around, {current_num_of_beers} on the wall")
	# print(after_drinking_string)
	
	while current_num_of_beers > 0:
		current_num_of_beers = 99
		print(before_drinking_string)
		current_num_of_beers -= 1
		print(after_drinking_string)

bottle_song()
