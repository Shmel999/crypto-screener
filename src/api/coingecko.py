import requests

class CoinGeckoAPI:
    BASE_URL = 'https://api.coingecko.com/api/v3'

    def get_crypto_price(self, id):
        """Fetch the current price of a cryptocurrency by ID."""
        url = f"{self.BASE_URL}/simple/price?ids={{id}}&vs_currencies=usd"
        response = requests.get(url)
        return response.json()

    def search_crypto(self, query):
        """Search for cryptocurrencies by name."""
        url = f"{self.BASE_URL}/coins/markets?vs_currency=usd&order=market_cap_desc&per_page=10&page=1&sparkline=false"
        response = requests.get(url)
        data = response.json()
        return [coin for coin in data if query.lower() in coin['name'].lower()]

    def get_trending(self):
        """Fetch trending cryptocurrencies."""
        url = f"{self.BASE_URL}/search/trending"
        response = requests.get(url)
        return response.json()