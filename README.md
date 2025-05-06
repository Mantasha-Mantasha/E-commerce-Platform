# Flask E-Commerce API

This is a simple E-Commerce API built with Flask. It provides functionality for managing products, users, and orders using in-memory data storage.

## Features

- **Products**
  - Add new products
  - Retrieve a list of all products
- **Users**
  - Add new users
  - Retrieve a list of all users
- **Orders**
  - Create new orders
  - Retrieve a list of all orders
  - Automatically deduct stock from products when an order is created

## Getting Started

### Prerequisites

- Python 3.7 or later
- Flask library

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/flask-ecommerce-api.git
   cd flask-ecommerce-api
   ```

2. Create a virtual environment and activate it:

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:

   ```bash
   pip install flask
   ```

4. Run the application:

   ```bash
   python app.py
   ```

5. The API will be available at `http://127.0.0.1:5000`.

## API Endpoints

### Products

- **GET /products**  
  Retrieve a list of all products.  
  **Response:**
  ```json

