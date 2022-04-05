import wikipedia
import webbrowser
import requests
from bs4 import BeautifulSoup

def wikiResult(query):
	query = query.replace('wikipedia','')
	query = query.replace('search','')
	if len(query.split())==0: query = "wikipedia"
	try:
		return wikipedia.summary(query, sentences=2)
	except Exception as e:
		return "Desired Result Not Found"

def latestNews(news=5):
	URL = 'https://indianexpress.com/latest-news/'
	result = requests.get(URL)
	src = result.content

	soup = BeautifulSoup(src, 'html.parser')

	headlineLinks = []
	headlines = []

	divs = soup.find_all('div', {'class':'title'})

	count=0
	for div in divs:
		count += 1
		if count>news:
			break
		a_tag = div.find('a')
		headlineLinks.append(a_tag.attrs['href'])
		headlines.append(a_tag.text)

	return headlines,headlineLinks

def openWebsite(url='https://www.google.com/'):
	webbrowser.open(url)

def jokes():
	URL = 'https://icanhazdadjoke.com/'
	result = requests.get(URL)
	src = result.content

	soup = BeautifulSoup(src, 'html.parser')

	try:
		p = soup.find('p')
		return p.text
	except Exception as e:
		raise e

def googleSearch(query):
	if 'image' in query:
		query += "&tbm=isch"
	query = query.replace('images','')
	query = query.replace('image','')
	query = query.replace('search','')
	query = query.replace('show','')
	query = query.replace('google','')
	query = query.replace('browse','')
	webbrowser.open("https://www.google.com/search?q=" + query)
	return "Here you go..."

def quiz(query):
	remove_list = ['test','quiz','exam','assessment','examination','examine','on','in','the','is','for','from',' ']
	query = query.split(' ')
	query_temp = query.copy()
	for word in query: # quiz on python  test test python
		print("In the for loop",word, word in remove_list)
		if word in remove_list:
			print(word)
			try:
				query_temp.remove(word)
			except Exception as e:
				pass
	query = ''.join(query_temp)
	print(query, query_temp)
	if query.lower() in ['dbms','python','programming','oops']:
		webbrowser.open("http://127.0.0.1:8000/home/quiz/" + query.lower())
		return "All the best!"
	else:
		return f"Sorry, we  don't have questions for {query} yet."
