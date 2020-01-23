

"""
Collin Seaman
1/16/2020

This script accepts a wsjInfoClass object and maps it to a csv file.

For reference, see the wsjInfoClass declaration copied from WSJ_Rankings.py pasted below:

class wsjRankingsClass:
	def __init__(print(len(wsjInfo):
		print(len(wsjInfo.rank))
		print(len(wsjInfo.college))
		print(len(wsjInfo.outcomes))
		print(len(wsjInfo.resources))
		print(len(wsjInfo.engagement))
		print(len(wsjInfo.environment))
		print(len(wsjInfo.average_net_price))
		#Details
		print(len(wsjInfo.overall_score))
		print(len(wsjInfo.outcomes_score))
		print(len(wsjInfo.resources_score))
		print(len(wsjInfo.engagement_score))
		print(len(wsjInfo.environment_score))
		print(len(wsjInfo.enrollment))
		print(len(wsjInfo.studentfac_ratio))
		print(len(wsjInfo.spending_per_student))
		print(len(wsjInfo.tuition))
		print(len(wsjInfo.room_and_board))
		print(len(wsjInfo.salary_10_years_after))
		print(len(wsjInfo.default_rate))
		print(len(wsjInfo.debt_after_grad))
"""

from WSJ_Rankings import getWSJInfo
import pandas

wsjInfo = getWSJInfo()

print("Lengths:")
print(len(wsjInfo.college))
print(len(wsjInfo.outcomes))
print(len(wsjInfo.resources))
print(len(wsjInfo.engagement))
print(len(wsjInfo.environment))
print(len(wsjInfo.average_net_price))
#Details
print(len(wsjInfo.overall_score))
print(len(wsjInfo.outcomes_score))
print(len(wsjInfo.resources_score))
print(len(wsjInfo.engagement_score))
print(len(wsjInfo.environment_score))
print(len(wsjInfo.enrollment))
print(len(wsjInfo.studentfac_ratio))
print(len(wsjInfo.spending_per_student))
print(len(wsjInfo.tuition))
print(len(wsjInfo.room_and_board))
print(len(wsjInfo.salary_10_years_after))
print(len(wsjInfo.default_rate))
print(len(wsjInfo.debt_after_grad))

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

output_file_name = 'Output Tables\\WSJrankings.xlsx'
df.to_excel(output_file_name, index=False, encoding='utf-8')

print('Output file ' + output_file_name + ' created!')