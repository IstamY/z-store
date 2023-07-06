
# Z-STORE

This is a Django-based e-commerce website project.

## Description

The project aims to create an e-commerce platform where users can browse products, add them to their cart, and place orders. The website provides a user-friendly interface for customers to explore and purchase products.

## Features

- User registration and authentication
- Product catalog with categories and search functionality
- Cart functionality for adding/removing products
- Checkout process for placing orders
- Order management for administrators
- User-friendly admin panel for managing products, categories, and orders

## Installation

1. Clone the repository:
   ```
   git clone <repository_url>
   ```

2. Create a virtual environment:
   ```
   python -m venv myenv
   ```

3. Activate the virtual environment:
   - For Windows:
     ```
     myenv\Scripts\activate
     ```
   - For Linux/macOS:
     ```
     source myenv/bin/activate
     ```

4. Install the dependencies:
   ```
   pip install -r requirements.txt
   ```

5. Apply migrations:
   ```
   python manage.py migrate
   ```

6. Start the development server:
   ```
   python manage.py runserver
   ```

7. Access the website at `http://localhost:8000` in your web browser.

## Usage

- Visit the website homepage to browse products and add them to the cart.
- Register an account or log in if you already have one.
- Proceed to the cart, review the items, and proceed to the checkout process.
- Fill in the required information and select a payment method to place the order.
- Administrators can log in to the admin panel (`/admin`) to manage products, categories, and orders.

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, please create a pull request or submit an issue.

## Credits

- [Django](https://www.djangoproject.com/) - Web framework used for development.
- [Bootstrap](https://getbootstrap.com/) - CSS framework for styling the website.
- [PostgreSQL](https://www.postgresql.org/) - Relational database used for data storage.

Feel free to customize this README.md file to include specific details about your project.