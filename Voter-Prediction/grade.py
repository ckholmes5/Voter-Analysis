# To Do:
state_dict = {'Florida': {}}

class grade_submission(object):
	"""
	Takes in submission, voter file, and state, and grades submission.
	Submission should have two columns, voter_id and pred_voted (1/0). 
	Voter file should have two columns, voter_id and actual_voted (1/0). 

	pct_correct: returns proportion of correctly predicted votes
	num_voters: returns number of voters in submission (useful for aggregating multiple voter files)


	"""
	def __init__(self, submission, voter_file):
		self.submission = submission
		self.voter_file = voter_file
		self.state = state
		self.merge_submission()
		self.calc_pct_correct()
		self.num_voters()

	def merge_submission(self):
		self.merged = self.submission.merge(self.voter_file, how = 'outer')
		self.merged['actual_voted'] = self.merged['actual_voted'].fillna(0)

	def calc_pct_correct(self):
		def check_pred(x):
		    correct = 0
		    if x['actual_voted'] == 1:
		        if x['pred_voted'] == 1:
		            correct = 1
		    if x['actual_voted'] == 0:
		        if x['pred_voted'] == 0:
		            correct = 1
		    return correct

		self.merged['correct'] = self.merged.apply(lambda x: check_pred(x), axis = 1)
		self.pct_correct = sum(self.merged['correct'])/float(len(self.merged))
    
	def num_voters(self):
		self.num_voters = len(self.submission)

# class total_grade(object):
# 	"""
# 	Takes in submission and state and outputs the overall score across 
# 	"""
# 	def __init__(self, stuff):
# 		self.stuff = stuff






