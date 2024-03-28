import sqlite3


class Restaurant:
    def __init__(self, restaurant_id, name, price):
        self.id = restaurant_id
        self.name = name
        self.price = price
        self.reviews = []  # Initialize an empty list to store reviews

    @classmethod
    def fanciest(cls):
        """
        Returns one restaurant instance for the restaurant that has the highest price.
        """
        conn = sqlite3.connect('restaurant.db')
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM restaurants ORDER BY price DESC LIMIT 1")
        restaurant_data = cursor.fetchone()
        conn.close()
        
        if restaurant_data:
            return cls(*restaurant_data)
        else:
            return None

    def load_reviews(self):
        """
        Loads all reviews for this restaurant from the database and populates self.reviews.
        """
        conn = sqlite3.connect('restaurant.db')
        cursor = conn.cursor()
        cursor.execute("""
            SELECT star_rating, comment
            FROM reviews
            WHERE restaurant_id = ?
        """, (self.id,))
        reviews_data = cursor.fetchall()
        conn.close()

        self.reviews = [Review(*review_data) for review_data in reviews_data]

    def all_reviews(self):
        """
        Returns a list of strings with all the reviews for this restaurant formatted as specified.
        """
        return [f"Review for {self.name} by {review.author}: {review.rating} stars." for review in self.reviews]

    def customers(self):
        """
        Returns a collection of all the customers who reviewed the Restaurant.
        """
        conn = sqlite3.connect('restaurant.db')
        cursor = conn.cursor()
        cursor.execute("""
            SELECT DISTINCT customers.*
            FROM customers
            JOIN reviews ON customers.id = reviews.customer_id
            WHERE reviews.restaurant_id = ?
        """, (self.id,))
        customers_data = cursor.fetchall()
        conn.close()
        return [Customer(*customer_data) for customer_data in customers_data]

from Review import Review 
from Customer import Customer  