

"""
Collin Seaman
1/16/2020

This script accepts a wsjInfoClass object and maps it to a csv file.

For reference, see the wsjInfoClass declaration copied from WSJ_Rankings.py pasted below:

class wsjInfoClass:
	def __init__(self):
		self.rank = []
		self.college = []
		self.outcomes = []
		self.resources = []
		self.engagement = []
		self.environment = []
		self.average_net_price = []
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
	'Average Net Price': wsjInfo.average_net_price
	})

output_file_name = 'WSJrankings.csv'
df.to_csv(output_file_name, index=False, encoding='utf-8')

print('Output file ' + output_file_name + ' created!')