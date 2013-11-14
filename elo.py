
# how do i go about making this a usable module
# are there scoping issues, variable naming conventions i should follow
# code review
# float - is there a better way?
# python 2.7 vs 3 compatibility

# move to wihtin object
# from __future__ imoport div
# talk to katie pip 

# USER SET K VALUE BASED ON USE CASE
K_VALUE = 32


def new_ratings(player1_rating,player2_rating,result,k_value=K_VALUE,should_round=True):
	#Assign actual individual results
   player1_result = result
   player2_result = 1 - result

   #Calculate expected results
   player1_expectation = 1/(1+10**((player2_rating - player1_rating)/400.0)) #the .0 is important to force float operations!))
   player2_expectation = 1/(1+10**((player1_rating - player2_rating)/400.0))

	#Calculate new ratings
   player1_new_rating = player1_rating + (k_value*(player1_result - player1_expectation))
   player2_new_rating = player2_rating + (k_value*(player2_result - player2_expectation))

   #Optional rounding
   if should_round:
      # int rounds down and forces type
      player1_new_rating = int(player1_new_rating)
      player2_new_rating = int(player2_new_rating) 

   # Create a dictionary to return and do so!
   new_ratings = dict()
   new_ratings['player1'] = player1_new_rating
   new_ratings['player2'] = player2_new_rating
   return new_ratings


class RatedPlayer(object):
   """A rated player"""
   def __init__(self,id,rating):
      self.id = id
      self.rating = rating

class Match(object):
   """Match"""
   def __init__(self,player1,player2,result):
      ratings_after_match = new_ratings(player1.rating,player2.rating,result)
      player1.rating = ratings_after_match['player1']
      player2.rating = ratings_after_match['player2']


# OOP
tom = RatedPlayer("Tom",1600)
alan = RatedPlayer("Alan",2000)
print tom.rating
print alan.rating
Match(tom,alan,1)
print tom.rating
print alan.rating
print 

# procedural
tomRating = 1600
alanRating = 2000
print tomRating
print alanRating
after_match_ratings = new_ratings(tomRating,alanRating,1)
tomRating = after_match_ratings["player1"]
alanRating = after_match_ratings["player2"]
print tomRating
print alanRating

