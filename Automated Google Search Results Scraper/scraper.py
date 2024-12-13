import requests
from bs4 import BeautifulSoup

def scrape_google_results(query):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }
    url = f"https://www.google.com/search?q={query.replace(' ', '+')}&hl=en"
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")
    
    results = []
    for g in soup.select(".tF2Cxc"):
        title = g.select_one(".DKV0Md").text if g.select_one(".DKV0Md") else "No Title"
        link = g.select_one(".yuRUbf a")["href"] if g.select_one(".yuRUbf a") else "No Link"
        description = g.select_one(".VwiC3b").text if g.select_one(".VwiC3b") else "No Description"
        results.append({"title": title, "link": link, "description": description})
    
    return results
