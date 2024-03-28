from Customer import Customer
from Restaurant import Restaurant
from Review import Review

def main():
    try:
        # Create some sample data to test
        customer1 = Customer(1, "Rachael", "NJoki")
        customer2 = Customer(2, "Peter", "Macharia")

        restaurant1 = Restaurant(1, "Pepinos 1", 50)
        restaurant2 = Restaurant(2, "Wa Kalucy 2", 60)

        review1 = Review(1, 1, 1, 5)
        review2 = Review(2, 2, 1, 4)
        review3 = Review(3, 1, 2, 3)

        # Testing methods for Customer
        print("Testing methods for Customer:")
        print("Full Name of Customer 1:", customer1.full_name())
        print("Full Name of Customer 2:", customer2.full_name())

        # Check if favorite restaurant is None before accessing its name attribute
        favorite_restaurant_1 = customer1.favorite_restaurant()
        if favorite_restaurant_1:
            print("Favorite Restaurant of Customer 1:", favorite_restaurant_1.name)
        else:
            print("Customer 1 has no favorite restaurant.")

        favorite_restaurant_2 = customer2.favorite_restaurant()
        if favorite_restaurant_2:
            print("Favorite Restaurant of Customer 2:", favorite_restaurant_2.name)
        else:
            print("Customer 2 has no favorite restaurant.")

        # Adding a new review for a restaurant by a customer
        customer1.add_review(restaurant1, 4)

        # Displaying all reviews for a restaurant
        print("All Reviews for Restaurant 1:")
        reviews_1 = restaurant1.all_reviews()
        for review in reviews_1:
            print(review)

        # Deleting all reviews for a restaurant by a customer
        customer1.delete_reviews(restaurant1)

        # Displaying all reviews for a restaurant again to confirm deletion
        print("All Reviews for Restaurant 1 (after deletion):")
        reviews_1_after_deletion = restaurant1.all_reviews()
        for review in reviews_1_after_deletion:
            print(review)

        # Testing methods for Review
        print("\nTesting methods for Review:")
        print("Full Review:", review1.full_review())

        # Testing methods for Restaurant
        print("\nTesting methods for Restaurant:")
        fanciest_restaurant = Restaurant.fanciest()
        if fanciest_restaurant:
            print("Fanciest Restaurant:", fanciest_restaurant.name)
        else:
            print("No restaurants available.")

    except ValueError as e:
        print("Error:", e)

if __name__ == "__main__":
    main()
