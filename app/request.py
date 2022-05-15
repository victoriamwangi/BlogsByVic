import urllib.request, json
from .models import Quote


def get_quotes():
    quotes_url = 'http://quotes.stormconsultancy.co.uk/random.json'
    with urllib.request.urlopen(quotes_url) as url:
        quotes_details= url.read()
        quotes_details_response = json.loads(quotes_details)
        
        print(quotes_details_response)
