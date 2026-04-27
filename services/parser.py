import requests
from bs4 import BeautifulSoup

def parse_amazon(url):
    try:
        headers = {"User-Agent": "Mozilla/5.0"}
        res = requests.get(url, headers=headers)
        soup = BeautifulSoup(res.text, "html.parser")

        title = soup.find(id="productTitle")
        title = title.get_text(strip=True) if title else ""

        bullets = soup.select("#feature-bullets li span")
        bullets = [b.get_text(strip=True) for b in bullets]

        return {
            "title": title,
            "bullets": bullets
        }

    except:
        return {"error": "Failed to scrape"}