"""
Collin Seaman
1/16/2020

This script provides functions for parsing the college rankings from the Wall Street Journal website.
Make sure you have all the following files in the same directory as this one:
	xpath_soup.py
	1.0.7_0 folder (contains adblocker)
	chromedriver.exe

Required Packages: 
	BeautifulSoup 4
	Selenium
	
"""

import requests
from bs4 import BeautifulSoup
from xpath_soup import xpath_soup
import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys

class wsjRankingsClass:
	def __init__(self):
		self.rank = []
		self.college = []
		self.outcomes = []
		self.resources = []
		self.engagement = []
		self.environment = []
		self.average_net_price = []

class pageInfoClass:
	def __init__(self):
		pass
# This function initializes and opens a chrome window controlled by selenium
# It takes no arguments and returns a pageInfo object, which contains:
# 1. driver (selenium-created object for controlling clicks)
# 2. soup (BeautifulSoup object containing the entire page)
# 3. table_soup (BeautifulSoup object containing just the rankings table)
def initialize_driver():
	pageInfo = pageInfoClass()
	working_directory = os.getcwd();
	path_to_extention = working_directory + "\\1.0.7_0"
	url = "https://www.wsj.com/articles/explore-the-full-wsj-the-college-rankings-11567638555"
	chrome_options = Options()
	chrome_options.add_argument('load-extension=' + path_to_extention)
	pageInfo.driver = webdriver.Chrome(options=chrome_options)
	pageInfo.driver.create_options()
	pageInfo.driver.get(url)
	content = pageInfo.driver.page_source
	pageInfo.soup = BeautifulSoup(content, features="html.parser")
	pageInfo.table_soup = pageInfo.soup.find('tbody')
	return pageInfo

# This function parses the rankings table inside table_soup iteratively
# It returns a wsj_Rankings object

def getWSJInfo():

	wsj_rankings = wsjRankingsClass()
	pageInfo = initialize_driver()

	# Sometimes the table does not load, not sure why but this re-initializes if it doesn't
	while(not pageInfo.soup.find('tbody')):
		pageInfo = initialize_driver()

	soup = pageInfo.soup
	table_soup = pageInfo.table_soup
	driver = pageInfo.driver

	next_button_soup = soup.find("li", {"title":"next page"})
	next_button_xpath = xpath_soup(next_button_soup)
	next_button_driver = driver.find_elements_by_xpath(next_button_xpath)[0]

	html = driver.find_element_by_tag_name('html')

	print('Getting rankings...')

	repeat = 0
	# This loop iterates over each page of the table, terminating when the next button indicates there are no more pages
	while(1):
		#This loop iterates over each row of the table and appends the columns to wsj_rankings
		for school in table_soup.findAll('tr'):
			
			#Check for empty rows
			if(len(school.findAll('td')) < 7):
				continue

			# If the next button is not in the window it cannot be clicked
			# If there are any repeat schools, this will scroll down a bit to reveal the button
			# This could probably be more efficient
			if(school.findAll('td')[4].get_text() in wsj_rankings.college):
				driver.execute_script("window.scrollTo(0, window.scrollY + 200)")
				break

			#print(school.findAll('td')[4].get_text())

			# If the order of information changes this must be changed
			school.find('td').extract()
			wsj_rankings.rank.append(school.find('td').extract().get_text())
			wsj_rankings.college.append(school.find('td').extract().get_text())
			wsj_rankings.outcomes.append(school.find('td').extract().get_text())
			wsj_rankings.resources.append(school.find('td').extract().get_text())
			wsj_rankings.engagement.append(school.find('td').extract().get_text())
			wsj_rankings.environment.append(school.find('td').extract().get_text())
			wsj_rankings.average_net_price.append(school.find('td').extract().get_text())

		#This moves to the next page of the table and updates soup and table_soup
		if(next_button_soup.attrs["class"][0] != "disabled"):
			next_button_driver.click()
			content = driver.page_source
			soup = BeautifulSoup(content, features="html.parser")
			table_soup = soup.find('tbody')
			next_button_soup = soup.find("li", {"title":"next page"})
			next_button_xpath = xpath_soup(next_button_soup)
			next_button_driver = driver.find_elements_by_xpath(next_button_xpath)[0]
		else: 
			break
	return wsj_rankings
