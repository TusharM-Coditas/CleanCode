# Cryptocurrency Tracker Application

A simple cryptocurrency tracker application that pulls real-time data from a public cryptocurrency API. This application allows users to monitor the performance of various cryptocurrencies, displaying their current prices, market caps, trading volumes, and price changes over different time periods.

## Features

- Show the current price, market cap, and trading volume for a specified cryptocurrency.
- Display price changes over various time periods (e.g., 24 hours, 7 days, 1 month).
- Compare multiple cryptocurrencies on the same metrics.
- Handle potential errors, such as invalid cryptocurrency names or API issues.

## Technologies Used

- Python 3.x
- `requests` library for API requests

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/TusharM-Coditas/CleanCode.git
   cd CleanCode/Python
2. Create a virtual environment (optional but recommended):
    ```
    python -m venv crypto_tracker_env
3. Activate the virtual environment:
    ##### On Windows
    ```
    crypto_tracker_env\Scripts\activate
4. Install the required dependencies:
    ```
    pip install requests
5. Run the application:
    ```
    python crypto_tracker.py