import pandas as pd
from state_dict import state_dict

# Feature Ideas
# 1. Generate % of presidential elections voter has voted in that they were registered for
# 2. Generate % of all elections voter could've voted in
# 3. Generate % 

class clean_data(object):
	"""
	voter_id: column name for voter id given a state name
	reg_date: column name for registration date given a state name

	"""
	def __init__(self, state, raw_data):
		self.voter_id = state_dict[state['voter_id']]
		self.reg_date = state_dict[state['reg_date']]
		self.raw_data = raw_data

	def find_stuff(self, ):

