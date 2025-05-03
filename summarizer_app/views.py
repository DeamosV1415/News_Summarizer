from django.shortcuts import render
import requests
from .summarizer import summarize_text

def home(request):
    NEWS_API_KEY = '7b70b4a448b84d0a8562c1331fa17e5b'
    url = (
    "https://newsapi.org/v2/top-headlines"
    "?country=us"
    "&pageSize=30"      
    f"&apiKey={NEWS_API_KEY}"
)
    response = requests.get(url)
    data = response.json()

    '''response = requests.get(url)                 
    print("NEWS API status:", response.status_code)
    data = response.json()
    print("NEWS API payload keys:", data.keys())
    print("First 5 articles:", data.get("articles", [])[:5])'''


    articles = []
    for article in data['articles'][:10]:
        content = article['description'] or article['content'] or ''
        if content:
            summary = summarize_text(content)
            articles.append({
                'title': article['title'],
                'url': article['url'],
                'summary': summary,
                'source': article['source']['name']
            })


    return render(request, 'index.html', {'articles': articles})