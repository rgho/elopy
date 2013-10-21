def new_ratings(player1_rating,player2_rating,k_value,result,should_round=False):
	#Assign actual individual results
	player1_result = result
	player2_result = 1 - result

	#Calculate expected results
	player1_chances = 1/(1+10^((player2_rating - player1_rating)/400))
   	player2_chances =  1/(1+10^((player1_rating - player2_rating)/400))

   	#Calculate new ratings
   	player1_new_rating = player1_rating + (k_value*(player1_result - player1_chances)) 
   	player2_new_rating = player2_rating + (k_value*(player2_result - player2_chances)) 
   	
   	#Optional rounding
   	if should_round:
   		player1_new_rating = round(player1_new_rating)
   		player2_new_rating = round(player2_new_rating) 

   	# Create a dictionary to return and do so!
   	new_ratings = dict()
   	new_ratings['player1'] = player1_new_rating
   	new_ratings['player2'] = player2_new_rating
   	return new_ratings