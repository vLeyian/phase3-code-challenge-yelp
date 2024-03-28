# review.py

import sqlite3

class Review:
    def __init__(self, id, restaurant_id, customer_id, star_rating):
        self.id = id
        self.restaurant_id = restaurant_id
        self.customer_id = customer_id
        self.star_rating = star_rating

    def full_review(self):
        """
        Returns a string formatted as follows: Review for {insert restaurant name} by {insert customer's full name}: {insert review star_rating} stars.
        """
        customer = self.customer()
        restaurant = self.restaurant()
        return f"Review for {restaurant.name} by {customer.full_name()}: {self.star_rating} stars."

    def customer(self):
        """
        Returns the Customer instance for this review.
        """
        conn = sqlite3.connect('restaurant.db')
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM customers WHERE id=?", (self.customer_id,))
        customer_data = cursor.fetchone()
        conn.close()
        if customer_data:
            return Customer(*customer_data)
        else:
            return None

    def restaurant(self):
        """
        Returns the Restaurant instance for this review.
        """
        conn = sqlite3.connect('restaurant.db')
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM restaurants WHERE id=?", (self.restaurant_id,))
        restaurant_data = cursor.fetchone()
        conn.close()
        if restaurant_data:
            return Restaurant(*restaurant_data)
        else:
            return None


from Customer import Customer
from Restaurant import Restaurant