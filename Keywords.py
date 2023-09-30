import requests #to get html requests and return as text
from bs4 import BeautifulSoup #for parsing and analyzing html content html=>text
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.probability import FreqDist
import string

def request(url):
    try:
        request = requests.get(url)
        request.raise_for_status() #r.status_code == 200 worse error checker
        return request.text
    except requests.exceptions.RequestException as e:
        print(f'Error: {e}')
        return None

def extract_keywords(web_content):
        if web_content is not None:
            soup = BeautifulSoup(web_content, 'html.parser')
            #turns the html into a string of words
            texts = soup.get_text()

            #changes text - tokenizes the string into a list of words
            text = word_tokenize(texts)

            #removing stopwords like an, a, etc
            stopword = set(stopwords.words('english'))
            filtered_text = [word.lower() for word in text if word.isalnum() and word not in stopword]

            print('\nTotal Word Count: ', len(filtered_text))

            freq_dist = FreqDist(filtered_text)
            print('\nTop 10 Keywords: ', freq_dist.most_common(10))
        else:
            print("Web content is unaccessible/ empty.")

link = input("Enter url for keyword analysis:")
extract_keywords(request(link))
