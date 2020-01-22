

"""
Collin Seaman
1/16/2020

This script accepts a wsjInfoClass object and maps it to a csv file.

For reference, see the wsjInfoClass declaration copied from WSJ_Rankings.py pasted below:

class wsjRankingsClass:
	def __init__(self):
		self.rank = []
		self.college = []
		self.outcomes = []
		self.resources = []
		self.engagement = []
		self.environment = []
		self.average_net_price = []
		#Details
		self.overall_score = []
		self.outcomes_score = []
		self.resources_score = []
		self.engagement_score = []
		self.environment_score = []
		self.enrollment = []
		self.studentfac_ratio = []
		self.spending_per_student = []
		self.tuition = []
		self.room_and_board = []
		self.salary_10_years_after = []
		self.default_rate = []
		self.debt_after_grad = []
"""

from WSJ_Rankings import getWSJInfo
import pandas

wsjInfo = getWSJInfo()

df = pandas.DataFrame({
	'Overall Ranking': wsjInfo.rank, 
	'College Name': wsjInfo.college,
	'Outomes Ranking': wsjInfo.outcomes,
	'Resources Ranking': wsjInfo.resources,
	'Engagement Ranking': wsjInfo.engagement,
	'Environment Ranking': wsjInfo.environment,
	'Average Net Price': wsjInfo.average_net_price,
	'Overall Score': wsjInfo.overall_score,
	'Outcomes Score': wsjInfo.outcomes_score,
	'Resources Score': wsjInfo.resources_score,
	'Engagement Score': wsjInfo.engagement_score,
	'Environment Score': wsjInfo.environment_score,
	'Enrollment': wsjInfo.enrollment,
	'Student-Faculty Ratio': wsjInfo.studentfac_ratio,
	'Academic Spending Per Student': wsjInfo.spending_per_student,
	'Tuition and Fees': wsjInfo.tuition,
	'Room and Board': wsjInfo.room_and_board,
	'Average Net Price': wsjInfo.average_net_price,
	'Salary 10 years after entering college': wsjInfo.salary_10_years_after,
	'Default Rate': wsjInfo.default_rate,
	'Student Debt After Graduation': wsjInfo.debt_after_grad
	})

output_file_name = 'Output Tables\\WSJrankings.csv'
df.to_csv(output_file_name, index=False, encoding='utf-8')

print('Output file ' + output_file_name + ' created!')