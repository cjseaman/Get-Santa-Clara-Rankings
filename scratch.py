import requests
from bs4 import BeautifulSoup
import os

desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')

file_object = open(desktop + "\\" + "SCU-Rankings.txt", 'w')

#US NEWS SECTION

print('US News:\n')
file_object.write('US News:\n')

url = "https://www.usnews.com/best-colleges/santa-clara-university-1326/overall-rankings"
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36'}
response = requests.get(url, headers=headers)

soup = BeautifulSoup(response.text, "html.parser")

results = soup.find_all('div', class_="block-flush")

for row in results:
    unfiltered = row
    unfiltered_soup = BeautifulSoup(unfiltered.text, "html.parser")
    filtered = unfiltered_soup.find_all(text=True)

    for ranking in filtered:
        final = " ".join(ranking.split())
        # the while loop will leave a trailing space,
        # so the trailing whitespace must be dealt with
        # before or after the while loop
 #       while '  ' in final:
 #           final = final.replace('  ', ' ')

        if final.find('#') == -1:
            continue
        print(final)
        file_object.write(final + '\n')


#Niche Section

print('\nNiche:\n')
file_object.write('\nNiche:\n')

url = "https://www.niche.com/colleges/santa-clara-university/rankings/"
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36'}
response = requests.get(url, headers=headers)

soup = BeautifulSoup(response.text, "html.parser")

results_title = soup.find_all('div', class_="rankings-card__link__title")
results_number = soup.find_all('span', class_="rankings-card__link__rank__number")

row_number = 0
for row in results_title:
    unfiltered_title = row
    unfiltered_number = results_number[row_number]
    unfiltered_number_soup = BeautifulSoup(unfiltered_number.text, "html.parser")
    unfiltered_title_soup = BeautifulSoup(unfiltered_title.text, "html.parser")
    filtered_number = unfiltered_number_soup.find_all(text=True)
    filtered_title =  unfiltered_title_soup.find_all(text=True)

    final = '#' + filtered_number[0] + ' ' + filtered_title[0]

    print(final)
    file_object.write(final + '\n')
    row_number = row_number + 1

print('\n')
print('Saving to ' + desktop)
file_object.close()


