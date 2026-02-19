import requests
from bs4 import BeautifulSoup

def scrape_data(url):
    try:
        response = requests.get(url, verify=False)
        response.raise_for_status()  # Check for HTTP errors

        soup = BeautifulSoup(response.content, 'html.parser')

        # Extract title
        title = soup.title.string if soup.title else "No title found"
        print(f"Title: {title}")

        # Extract all paragraph texts
        paragraphs = soup.find_all('p')
        print("\nFirst 5 paragraphs:")
        for i, p in enumerate(paragraphs[:5]):
            print(f"{i+1}: {p.get_text().strip()}")

    except requests.exceptions.RequestException as e:
        print(f"Error fetching the webpage: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    # Default URL for testing
    url = "https://viso.ai/applications/computer-vision-in-surveillance-and-security/"
    scrape_data(url)
