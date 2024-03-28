# week3_code_challenge
## Overview
This project is a Restaurant Review System designed to manage relationships between customers, restaurants, and reviews. It provides functionalities to manage reviews left by customers for various restaurants, retrieve information about restaurants and customers, and perform aggregate operations such as finding the fanciest restaurant or the favorite restaurant of a customer.

## Database Setup:
The initia step entails setting up the necessary database tables. The schema includes tables for restaurants, customers, and reviews. The reviews table establishes relationships between restaurants, customers, and reviews, storing attributes such as restaurant_id, customer_id, and star_rating.

## Data Creation: 
The database is Populated with sample data by creating instances of the Restaurant and Customer classes. Main.py file is used to instantiate objects and store them in the database. This step is crucial for testing the functionalities of the system.

## Object Relationship Methods: 
Methods in the classes are created to establish relationships between entities. For instance, the reviews() method in the Restaurant class returns a collection of all reviews for the restaurant, while the restaurants() method in the Customer class returns restaurants reviewed by a specific customer.

## Aggregate and Relationship Methods: 
Methods are created to perform aggregate operations and retrieve relevant information. For example, the fanciest() method in the Restaurant class returns the restaurant with the highest price, and the favorite_restaurant() method in the Customer class identifies the favorite restaurant of a customer based on the highest star rating.

