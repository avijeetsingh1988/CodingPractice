# numbers = [1,2,3,4,5,6,7,8,9]
# val=(x**2 for x in numbers)
# # abc=map(lambda a:a*a,numbers)
# print(next(val))
# print(next(val))


# class Restaurant:
#     def __init__(self, restaurant_name, cuisine_type):
#         self.restaurant_name = restaurant_name
#         self.cuisine_type = cuisine_type
#         self.number_served=0

#     def describe_restaurant(self):
#         print(f"The name of the restaurant is {self.restaurant_name}")
#         print(f"The cuisine is {self.cuisine_type}")

#     def served(self):
#         print(f"Number of people served {self.number_served}")

#     def set_number_served(self,set_number):
#         self.number_served=set_number
    
#     def increment_number_served(self,increment_number):
#         self.number_served=self.number_served + increment_number
        
#     def open_restaurant(self):
#         print(f"The restaurant {self.restaurant_name} is open")

# my_restaurant= Restaurant("East India Company","Indian")
# my_restaurant.describe_restaurant()
# my_restaurant.served()
# my_restaurant.number_served=10
# my_restaurant.served()
# my_restaurant.set_number_served(20)
# my_restaurant.served()
# my_restaurant.increment_number_served(10)
# my_restaurant.served()

# my_restaurant.open_restaurant()

# his_restaurant= Restaurant("Forenzo","Italian")
# her_restaurant= Restaurant("Laziz","Paki")
# his_restaurant.describe_restaurant()
# her_restaurant.describe_restaurant()

class User:
    def __init__(self,first_name,last_name,age):
        self.first_name=first_name
        self.last_name=last_name
        self.age=age
        self.login_attempts=0

    def describe_user(self):
        print(f"The name of the user is {self.first_name} {self.last_name} and is {self.age} years old")

    def greet_user(self):
        print(f"Hello {self.first_name} {self.last_name}, how are you doing today? ")

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts=0

my_user=User("John","Doe",31)
my_user.describe_user()
my_user.greet_user()
my_user.increment_login_attempts()
my_user.increment_login_attempts()
my_user.increment_login_attempts()
my_user.increment_login_attempts()
print(f"Login attempts: {my_user.login_attempts}")
my_user.reset_login_attempts()
print(f"Login attempts: {my_user.login_attempts}")