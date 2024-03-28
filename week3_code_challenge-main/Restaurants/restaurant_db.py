import sqlite3

# Establish connection to the database
conn = sqlite3.connect('restaurant.db')

# Creating tables
conn.execute('''
    CREATE TABLE IF NOT EXISTS restaurants (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        price INTEGER
    );
''')

conn.execute('''
    CREATE TABLE IF NOT EXISTS customers (
        id INTEGER PRIMARY KEY,
        first_name TEXT,
        last_name TEXT
    );
''')

conn.execute('''
    CREATE TABLE IF NOT EXISTS reviews (
        id INTEGER PRIMARY KEY,
        restaurant_id INTEGER,
        customer_id INTEGER,
        star_rating INTEGER,
        FOREIGN KEY(restaurant_id) REFERENCES restaurants(id),
        FOREIGN KEY(customer_id) REFERENCES customers(id)
    );
''')

# Sample data for restaurants, customers, and reviews
restaurants_data = [
    ('Pepinos', 1),
    ('KFC', 2),
    ('Wa Kalucy', 3)
]

customers_data = [
    ('Rachael', 'Njoki'),
    ('Rockie', 'Rocks'),
    ('Peter', 'Macharia')
]

reviews_data = [
    (1, 1, 4),
    (2, 2, 3),
    (3, 3, 5)
]

# Insert data into restaurants table
for restaurant in restaurants_data:
    conn.execute("INSERT INTO restaurants (name, price) VALUES (?, ?)", restaurant)

# Insert data into customers table
for customer in customers_data:
    conn.execute("INSERT INTO customers (first_name, last_name) VALUES (?, ?)", customer)

# Insert data into reviews table
for review in reviews_data:
    conn.execute("INSERT INTO reviews (restaurant_id, customer_id, star_rating) VALUES (?, ?, ?)", review)

# Commit changes and close connection
conn.commit()
conn.close()
