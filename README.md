# Trading Platform Backend

A Django REST API backend for a trading platform.

## Features

- User accounts management
- Order placement and management
- Trade execution tracking
- Portfolio and holdings management

## Setup

1. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

2. Run migrations:
   ```
   python manage.py migrate
   ```

3. Create a superuser:
   ```
   python manage.py createsuperuser
   ```

4. Run the server:
   ```
   python manage.py runserver
   ```

## API Endpoints

- `/api/orders/` - Manage orders
- `/api/trades/` - View trades
- `/api/portfolios/` - Manage portfolios
- `/api/holdings/` - Manage holdings

## Models

- **Order**: Represents buy/sell orders
- **Trade**: Represents executed trades
- **Portfolio**: User's investment portfolio
- **Holding**: Individual stock holdings in a portfolio
