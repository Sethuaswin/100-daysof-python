# Creating Class called User
class User:
    #  pass   # This will create empty class to avoid the error

    # Creating Attributes assoisiates with User Class
    def __init__(self, user_id, user_name):  # This is called constructor also
        # Intialize
        self.id = user_id
        self.user_name = user_name
        # The Followers count
        self.followers = 0
        # The User Following count
        self.following = 0

    # Creating methods assosoated with the User class
    def follow(self, user):  # always have a self parameter as first
        # Number of followers is follwing the user
        user.followers += 1
        # Numbser of people user is following
        self.following += 1


# Intializing two users
user_1 = User("001", "aswin")  # The first value will be user_id etc..
user_2 = User("002", "jack")

# Calling the follow() methods for followers
user_1.follow(user_2)

print(f"user_1 followers = {user_1.followers}")
print(f"user_1 following = {user_1.following}")
print(f"user_2 followers = {user_2.followers}")
print(f"user_2 following = {user_2.following}")
