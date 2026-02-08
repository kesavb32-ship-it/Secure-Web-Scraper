"""from urllib.robotparser import RobotFileParser

def check_robots(url):
    rp = RobotFileParser()
    rp.set_url(url + "/robots.txt")
    rp.read()
    return rp.can_fetch("*", url)

urls = [
    "https://en.wikipedia.org/wiki/Scrapy?",
    "https://www.geeksforgeeks.org/websites-apps/history-of-internet/"
]

for url in urls:
    if check_robots(url):
        print(f"Scraping is ALLOWED on {url}")
    else:
        print(f"Scraping is NOT allowed on {url}")"""


"""import requests

def fetch_page(url):
    try:
        response = requests.get(url, verify=True)
        if response.status_code == 200:
            return response.text
        else:
            return None
    except requests.exceptions.SSLError as e:
        print(f"SSL Error: {e}")
        return None

url = "https://www.geeksforgeeks.org/websites-apps/history-of-internet/"
html_content = fetch_page(url)
if html_content:
    print("Page fetched successfully!")
else:
    print("Failed to fetch page.")


from bs4 import BeautifulSoup

def extract_data(html):
    soup = BeautifulSoup(html, 'html.parser')
    data = [p.text for p in soup.find_all('p')]
    return data

sample_html = 
<html>
    <body>
        <p>Python is a high-level programming language.</p>
        <p>It is widely used for web scraping and data analysis.</p>
        <p>BeautifulSoup helps parse HTML easily.</p>
    </body>
</html>


paragraphs = extract_data(sample_html)

print("Extracted Paragraphs:")
for p in paragraphs:
    print("-", p)"""



"""import pandas as pd

def save_data(data, filename="output.csv"):
    df = pd.DataFrame(data, columns=["Content"])
    df.to_csv(filename, index=False)

data = ["Paragraph 1 text", "Paragraph 2 text", "Paragraph 3 text"]
save_data(data, "output.csv")"""


import requests
from bs4 import BeautifulSoup
import pandas as pd

def fetch_page(url):
    try:
        response = requests.get(url, verify=True)  
        if response.status_code == 200:
            return response.text
        else:
            print(f"Failed to fetch page. Status code: {response.status_code}")
            return None
    except requests.exceptions.SSLError as e:
        print(f"SSL Error: {e}")
        return None
    except Exception as e:
        print(f"Error fetching page: {e}")
        return None

def extract_data(html):
    soup = BeautifulSoup(html, 'html.parser')
    paragraphs = [p.text.strip() for p in soup.find_all('p') if p.text.strip() != '']
    return paragraphs

def save_data(data, filename="output.csv"):
    df = pd.DataFrame(data, columns=["Content"])
    df.to_csv(filename, index=False)
    print(f"\nData saved to {filename}")

if __name__ == "__main__":
    url = "https://www.geeksforgeeks.org/websites-apps/history-of-internet/"  
    print(f"Fetching HTML from: {url}\n")
    
    html_content = fetch_page(url)
    if html_content:
        print("HTML fetched successfully.\nExtracting paragraphs...\n")
        extracted_paragraphs = extract_data(html_content)
        
        for i, para in enumerate(extracted_paragraphs[:5], start=1):
            print(f"Paragraph {i}: {para}\n")
        
        save_data(extracted_paragraphs)
    else:
        print("No content fetched.")




