import requests
from bs4 import BeautifulSoup
import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import pandas


rank = []
college = []
outcomes = []
resources = []
engagement = []
environment = []
average_net_price = []

working_directory = os.getcwd();

path_to_extention = working_directory + "\\1.0.7_0"

chrome_options = Options()
chrome_options.add_argument('load-extension=' + path_to_extention)
driver = webdriver.Chrome(options=chrome_options)
driver.create_options()

driver.get("https://www.wsj.com/articles/explore-the-full-wsj-the-college-rankings-11567638555")

content = driver.page_source
soup = BeautifulSoup(content, features="html.parser")


output = open('output.html', 'w', encoding="utf-8")

soup = soup.find('tbody')

print(soup, file = output)

#while(soup.find("li", {"title":"next page"}).attrs["class"][0] != "disabled"):
for school in soup.findAll('tr'):
	if(len(school.findAll('td')) < 7):
		print("skipped row")
		continue
	print("length: " + str(len(school.findAll('td'))))
	school.find('td').extract() #get rid of check mark
	rank.append(school.find('td').extract().get_text())
	college.append(school.find('td').extract().get_text())
	outcomes.append(school.find('td').extract().get_text())
	resources.append(school.find('td').extract().get_text())
	engagement.append(school.find('td').extract().get_text())
	environment.append(school.find('td').extract().get_text())
	average_net_price.append(school.find('td').extract().get_text())
	print(college)

df = pandas.DataFrame({
	'Overall Ranking': rank, 
	'College Name': college,
	'Outomes Ranking': outcomes,
	'Resources Ranking': resources,
	'Engagement Ranking': engagement,
	'Environment Ranking': environment,
	'Average Net Price': average_net_price
	})

df.to_csv('rankings.csv', index=False, encoding='utf-8')

