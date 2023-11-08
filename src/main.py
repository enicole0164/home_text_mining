import web_crawler
import text_mining
import search_urls

# Specify the target website URL
# url = 'https://www.meaningfullife.com/home-and-family/'  # Replace this with the target website URL
# url = 'https://www.nrc.no/perspectives/2020/seven-reasons-why-homes-for-refugees-are-more-important-than-you-think/'
# url = 'https://rightforeducation.org/2016/12/20/good-home-good-family/'

manual_links = [
    'https://www.intelligentchange.com/blogs/read/the-true-meaning-of-home',
    'https://www.schlage.com/blog/categories/2020/11/meaning-of-home.html',
    'https://medium.com/@persadaichwan/the-true-meaning-of-home-14683eb93abc',
    'https://kvf.fo/greinar/2023/05/03/true-meaning-home',
    'https://blog.coldwellbanker.com/the-origin-and-true-meaning-of-home/',
    'https://meaningofhome.ca/entries/27912',
    'https://www.meaningofhome.ca/entries/36677',
    'https://stephaniesillsrealty.com/blog/the-true-meaning-of-home'
]

search_query = 'true meaning home'  # You can customize the search query as needed

search_results = search_urls.search_related_urls(search_query)
links = [item['link'] for item in search_results]


for url in manual_links:
    print(f"Crawling {url}...")
    # Crawl the website
    website_text, success = web_crawler.crawl_website(url)
    
    if not success:
        continue

    # Analyze the text data
    word_counts = text_mining.analyze_text(website_text, 'home')

    # Print the most common words related to 'home'
    print("Most common words related to 'home':")
    print(word_counts)  # Change the number to display more or fewer words
