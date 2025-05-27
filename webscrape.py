import requests
from bs4 import BeautifulSoup
from duckduckgo_search import DDGS

def search_web(query, num_results=5):
    """Search the web using DuckDuckGo and return top result URLs."""
    with DDGS() as ddgs:
        results = list(ddgs.text(query, max_results=num_results))
    return [result["href"] for result in results if "href" in result]

def scrape_content(url):
    """Fetch and extract the main content from a webpage."""
    try:
        headers = {"User-Agent": "Mozilla/5.0"}
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()

        soup = BeautifulSoup(response.text, "html.parser")
        paragraphs = soup.find_all("p")

        content = "\n".join([p.get_text() for p in paragraphs if p.get_text()])
        return content # Return first 1000 characters for brevity
    except Exception as e:
        return f"Error fetching {url}: {e}"

def main():
    query = "How does AI work?"
    print(f"Searching for: {query}\n")

    search_results = search_web(query)
    
    if not search_results:
        print("No results found.")
        return
    
    for i, url in enumerate(search_results, start=1):
        print(f"\n{i}. Extracting content from: {url}")
        content = scrape_content(url)
        print(content, "...")  # Print first 500 characters

if __name__ == "__main__":
    main()
