import requests
from bs4 import BeautifulSoup

url = "https://news.ycombinator.com/newest"

response = requests.get(url)
html = response.text
# print(html)
soup = BeautifulSoup(html, "html.parser")

myLinks = soup.find_all("span", {"class": "titleline"})
# print(len(myLinks))
# print(myLinks)

find = ["replit", "python", "microsoft", "google", "apple"]

for link in myLinks:
  found = False
  temp = link.find_all("a")
  # print(link[0].text)
  text = temp[0].text
  result = text.lower()
  result = result.split()
  # print(result)
  # print(text)
  for word in result:
    if word in find:
      found=True
    
  if found: 
    print(text)
    print(temp[0]['href'])
    print()
