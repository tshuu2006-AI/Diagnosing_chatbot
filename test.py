import requests
from bs4 import BeautifulSoup
def scrape_scholarships():
    url = "https://vi.wikipedia.org/wiki/Ch%C3%B3"  # Replace with the actual URL
    response = requests.get(url)
    print(response.text)
    soup = BeautifulSoup(response.text, 'html.parser')
    print(soup.find_all('div', class_="cmsmasters_post_content entry-content"))
scrape_scholarships()
        