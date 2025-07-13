import requests
from bs4 import BeautifulSoup

def parse_data():
    url = "http://quotes.toscrape.com"
    response = requests.get(url)
    data_ = []
    quotes_data = []
    authors_data = []
    if response.status_code == 200:
        url_content = response.content
        soup = BeautifulSoup(url_content, "html.parser")
        quotes = soup.find_all('div', class_ = 'quote')
        author_links = []
        for quote in quotes:
            tags = [tag.text for tag in quote.find_all('a', class_ = 'tag')]
            author = quote.find('small', class_ = 'author').text
            text = quote.find('span', class_ = 'text').text
            quotes_data.append({
                'tags': tags,
                'author': author,
                'text': text
                })
            author_link = quote.find('a')['href']
            author_links.append(author_link)
        author_links = list(set(author_links))
        
        for author_link in author_links:
            author_response = requests.get(url + author_link)
            author_soup = BeautifulSoup(author_response.content, 'html.parser')
            fullname = author_soup.find('h3', class_ = 'author-title').text
            born_date = author_soup.find('span', class_ = 'author-born-date').text
            born_location = author_soup.find('span', class_ = 'author-born-location').text
            description = author_soup.find('div', class_ = 'author-description').text
            description = ' '.join(description.strip().split())
            authors_data.append({
                'fullname': fullname,
                'born_date': born_date,
                'born_location': born_location,
                'description': description
            })

        data_.append(quotes_data)
        data_.append(authors_data)

    return data_