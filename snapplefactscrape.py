from bs4 import BeautifulSoup as soup
import requests
import re

data = requests.get('https://www.snapple.com/real-facts')

output = open("snapplefacts.txt", "a")
soup = soup(data.text, 'html.parser')
facts = soup.select("#facts .description a")
for fact in facts:
    s = str(fact)
    number = re.search('<a href=(.*)>', s)
    result_number = re.findall(r'\d+', str(number))
    result = re.search('>(.*)<', s)
    result_final = str(result_number[2]) + "," + result.group(1)
    result_final_linebreak = result_final + "\n"
    output.write(result_final_linebreak)

print(output)