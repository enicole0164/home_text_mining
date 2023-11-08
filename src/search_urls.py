from googleapiclient.discovery import build

# Google Custom Search Engine (CSE) configuration
CSE_ID = '777f4f6afc8f54db0'
API_KEY = 'AIzaSyCt5CtF5TpbpKbHlAbvPvhpslKRp6FzniA'

# Function to perform a search and retrieve URLs
def search_related_urls(query):
    service = build("customsearch", "v1", developerKey=API_KEY)
    result = service.cse().list(q=query, cx=CSE_ID).execute()
    return result.get('items', [])

# Main function to search for 'home'-related URLs
def main():
    search_query = 'meaning of home'  # You can customize the search query as needed
    search_results = search_related_urls(search_query)

    # Print retrieved URLs
    for index, item in enumerate(search_results, start=1):
        print(f"{index}. {item['link']}")

if __name__ == "__main__":
    main()
