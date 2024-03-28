import sqlite3


class Customer:
    def __init__(self, customer_id, first_name, last_name):
        self.id = customer_id
        self.first_name = first_name
        self.last_name = last_name

    def full_name(self):
        """Returns the full name of the customer, with the first name and the last name concatenated, Western style."""
        return f"{self.first_name} {self.last_name}"

    def favorite_restaurant(self):
        """
        Returns the restaurant instance that has the highest star rating from this customer.
        """
        conn = sqlite3.connect('restaurant.db')
        cursor = conn.cursor()
        cursor.execute("""
            SELECT restaurants.* FROM restaurants
            JOIN reviews ON restaurants.id = reviews.restaurant_id
            WHERE reviews.customer_id=?
            ORDER BY reviews.star_rating DESC
            LIMIT 1
        """, (self.id,))
        restaurant_data = cursor.fetchone()
        conn.close()
        if restaurant_data:
            return Restaurant(*restaurant_data)
        else:
            return None

    def add_review(self, restaurant, rating):
        """
        Creates a new review for the restaurant with the given `restaurant_id`.
        """
        conn = sqlite3.connect('restaurant.db')
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO reviews (restaurant_id, customer_id, star_rating)
            VALUES (?, ?, ?)
        """, (restaurant.id, self.id, rating))
        conn.commit()
        conn.close()

    def delete_reviews(self, restaurant):
        """
        Removes all reviews for the given restaurant.
        """
        conn = sqlite3.connect('restaurant.db')
        cursor = conn.cursor()
        cursor.execute("""
            DELETE FROM reviews
            WHERE restaurant_id=? AND customer_id=?
        """, (restaurant.id, self.id))
        conn.commit()
        conn.close()

    def reviews(self):
        """
        Returns a collection of all the reviews that the Customer has left.
        """
        conn = sqlite3.connect('restaurant.db')
        cursor = conn.cursor()
        cursor.execute("""
            SELECT * FROM reviews
            WHERE customer_id=?
        """, (self.id,))
        reviews_data = cursor.fetchall()
        conn.close()
        return [Review(*review_data) for review_data in reviews_data]

    def restaurants(self):
        """
        Returns a collection of all the restaurants that the Customer has reviewed.
        """
        conn = sqlite3.connect('restaurant.db')
        cursor = conn.cursor()
        cursor.execute("""
            SELECT DISTINCT restaurants.*
            FROM restaurants
            JOIN reviews ON restaurants.id = reviews.restaurant_id
            WHERE reviews.customer_id=?
        """, (self.id,))
        restaurants_data = cursor.fetchall()
        conn.close()
        return [Restaurant(*restaurant_data) for restaurant_data in restaurants_data]

from Restaurant import Restaurant
from Review import Review