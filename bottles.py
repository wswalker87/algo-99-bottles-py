def bottle_song():
	current_num_of_beers = 99
	while current_num_of_beers > 0:
		if current_num_of_beers >= 2:
			before_drinking_string = (f"{current_num_of_beers} bottles of beer on the wall, {current_num_of_beers} bottles of beer.")
			print(before_drinking_string)
			current_num_of_beers -= 1
			after_drinking_string = (f"Take one down and pass it around, {current_num_of_beers} bottles of beer on the wall.")	
			print(after_drinking_string)
		elif current_num_of_beers == 1:
			one_more_bottle_string = (f"{current_num_of_beers} bottle of beer on the wall, {current_num_of_beers} bottle of beer.")
			print(one_more_bottle_string)
			current_num_of_beers -= 1
			last_bottle_string = (f"Take one down and pass it around, no more bottles of beer on the wall.")
			print(last_bottle_string)

	finished_drinking = "No more bottles of beer on the wall, no more bottles of beer."
	empty_drinking = "Go to the store and buy some more, 99 bottles of beer on the wall."
	print(finished_drinking)
	print(empty_drinking)
	


bottle_song()
