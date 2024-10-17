import requests

class CryptoTracker:
    """A class to track cryptocurrency data using the CoinGecko API."""
    
    BASE_URL = "https://api.coingecko.com/api/v3"

    def __init__(self):
        """Initialize an empty dictionary to store cryptocurrency data."""
        self.crypto_data = {}

    def fetch_data(self, cryptocurrency):
        """
        Fetch the current data for a given cryptocurrency.

        Args:
            cryptocurrency (str): The name of the cryptocurrency to fetch data for.

        Raises:
            ValueError: If the cryptocurrency name is invalid or not found.
            Exception: For general API request failures.
        """
        try:
            # Send a request to the CoinGecko API
            response = requests.get(f"{self.BASE_URL}/coins/markets", params={
                'vs_currency': 'usd',
                'ids': cryptocurrency,
                'order': 'market_cap_desc',
                'per_page': 1,
                'page': 1,
                'sparkline': False
            })

            # Check for a successful response
            if response.status_code == 200:
                data = response.json()
                if data:
                    self.crypto_data = data[0]  # Store the first result
                else:
                    raise ValueError("Cryptocurrency not found.")
            else:
                raise ValueError(f"Error fetching data: {response.status_code}")

        except ValueError as ve:
            print("ValueError:", ve)
        except requests.exceptions.RequestException as e:
            print("An error occurred with the API request:", str(e))
        except Exception as e:
            print("An unexpected error occurred:", str(e))

    def display_data(self):
        """
        Display the fetched cryptocurrency data.

        If no data has been fetched, print a message indicating so.
        """
        if not self.crypto_data:
            print("No data to display. Please fetch data first.")
            return

        # Display the fetched cryptocurrency information
        print(f"\nName: {self.crypto_data['name']}")
        print(f"Current Price: ${self.crypto_data['current_price']:.2f}")
        print(f"Market Cap: ${self.crypto_data['market_cap']:,}")
        print(f"24h Volume: ${self.crypto_data['total_volume']:,}")
        print(f"Price Change (24h): {self.crypto_data['price_change_percentage_24h']:.2f}%")

    def fetch_multiple(self, cryptocurrencies):
        """
        Fetch and display data for multiple cryptocurrencies.

        Args:
            cryptocurrencies (list): A list of cryptocurrency names.
        """
        for crypto in cryptocurrencies:
            print(f"\nFetching data for: {crypto}")
            self.fetch_data(crypto)
            self.display_data()

def main():
    """Main function to run the cryptocurrency tracker application."""
    tracker = CryptoTracker()
    
    while True:
        print("\nCryptocurrency Tracker")
        print("1. Fetch data for a single cryptocurrency")
        print("2. Fetch data for multiple cryptocurrencies")
        print("3. Exit")
        
        choice = input("Choose an option: ")
        
        if choice == '1':
            # Fetch data for a single cryptocurrency
            crypto_name = input("Enter the cryptocurrency name (e.g., bitcoin, ethereum): ").lower()
            tracker.fetch_data(crypto_name)
            tracker.display_data()
        elif choice == '2':
            # Fetch data for multiple cryptocurrencies
            crypto_names = input("Enter comma-separated cryptocurrency names (e.g., bitcoin, ethereum): ").lower().split(',')
            tracker.fetch_multiple([crypto.strip() for crypto in crypto_names])
        elif choice == '3':
            # Exit the application
            print("Exiting the application. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
