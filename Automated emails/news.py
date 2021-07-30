import requests
from pprint import pprint
import datetime

class Newsfeed:

    def __init__(self, interest, language='en'):
        self.interest = interest
        self.language = language
    
    def get(self):
        today = datetime.datetime.now().strftime('%Y-%m-%d')
        yesterday = (datetime.datetime.now() - datetime.timedelta(days=1)).strftime('%Y-%m-%d')
        api_key = '295298ca9d0749d880984e8f33f23694'
        base_url = 'https://newsapi.org/v2/everything?'
        url = f"{base_url}"\
            f"q={self.interest}&"\
            f"from={yesterday}&"\
            f"to={today}&"\
            f"language={self.language}&"\
            f"apiKey={api_key}"
        # print(url)
        response = requests.get(url)
        if response.json()['status'] == "ok":
            content = ""
            articles = response.json()['articles']

            index = 1
            for article in articles:
                content += f"{index}. {article['title']} \n {article['url']}\n\n"
                if(index >= 5):        #want only top five news
                    break
                index +=1
            return content
               
        else:
            f"status : {response.json()['status']}"
       
if __name__=="__main__":
    news = Newsfeed('Lucknow')
    content = news.get()
    