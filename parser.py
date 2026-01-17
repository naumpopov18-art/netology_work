import requests
import bs4

KEYWORDS = ['дизайн', 'фото', 'web', 'python']

response = requests.get("https://habr.com/ru/articles/")
soup = bs4.BeautifulSoup(response.text, 'lxml')

for article in soup.find_all('article'):
    h2 = article.find('h2')
    if not h2:
        continue
    
    a = h2.find('a')
    if not a:
        continue
    
    title = h2.text.strip()
    link = "https://habr.com" + a['href']
    
    time_tag = article.find('time')
    date = time_tag['title'] if time_tag and 'title' in time_tag.attrs else ""
    
    text_for_search = article.get_text().lower()
    
    for keyword in KEYWORDS:
        if keyword in text_for_search:
            print(f"{date} – {title} – {link}")
            break