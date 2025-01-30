import random
import datetime
def get_test_transactions(start_date, num_days, initial_price, volatility, num_transactions):
    """
    Generate a list of simulated buy and sell transactions.

    Parameters:
    - start_date (datetime.date): The starting date for transactions.
    - num_days (int): Number of days over which transactions occur.
    - initial_price (float): Starting price of the asset.
    - volatility (float): Maximum percentage change in price per day.
    - num_transactions (int): Total number of transactions to generate.

    Example usage:
      start_date = datetime.date(2025, 1, 1)
      transactions = get_test_transactions(start_date, num_days=30, initial_price=100.0, volatility=5.0, num_transactions=10)

      for transaction in transactions:
          print(transaction)

    Returns:
    - List[dict]: A list of transaction dictionaries with keys: 'date', 'type', 'price', 'quantity'.
    """
    transactions = []
    current_price = initial_price
    current_date = start_date

    for _ in range(num_transactions):
        # Randomly decide if the transaction is a buy or sell
        transaction_type = random.choice(['BUY', 'SELL'])

        # Simulate price change
        price_change = random.uniform(-volatility, volatility)
        current_price *= (1 + price_change / 100)

        # Ensure price doesn't drop below a certain threshold
        current_price = max(current_price, initial_price * 0.5)

        # Randomly determine quantity between 1 and 100 units
        quantity = random.randint(1, 100)

        # Append transaction to the list
        transactions.append({
            'date': current_date,
            'type': transaction_type,
            'price': round(current_price, 2),
            'quantity': quantity
        })

        # Move to the next day
        current_date += datetime.timedelta(days=random.randint(1, num_days // num_transactions))

    return transactions