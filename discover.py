import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin


def find_documents(url):
    try:
        # Fetch the webpage
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for HTTP status codes 4xx/5xx

        # Parse the webpage content
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Extract all links from the page
        links = [a['href'] for a in soup.find_all('a', href=True)]
        
        # Filter links to find documents based on their extensions
        documents = [urljoin(url, link) for link in links if link.lower().endswith(('.pdf', '.doc', '.xls', '.ppt'))]
        
        # Return the list of document URLs
        return documents
    
    except requests.RequestException as e:
        print(f"Request failed: {e}")
        return []

