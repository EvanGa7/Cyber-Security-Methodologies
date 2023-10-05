# Evan Gardner
# CS-450 Cyber Security
# Professor Weihao
# October 3, 2023
# Weekly Assignment 4

# This program is a Role Based Access Control (RBAC) system.
# It allows the user to create, delete, and modify users, roles, and permissions.

class User:
    def __init__(self, name, role):
        self.name = name
        self.role = role

class Role:
    def __init__(self, name, permissions):
        self.name = name
        self.permissions = permissions

class Permission:
    def __init__(self, movie_rating, release_type):
        self.movie_rating = movie_rating
        self.release_type = release_type

    def can_access(self, user_role):
        if self.movie_rating == "R" and user_role not in ["adult premium", "adult regular"]:
            return False
        if self.movie_rating == "PG-13" and user_role in ["child premium", "child regular"]:
            return False
        if self.release_type == "new" and "premium" not in user_role:
            return False
        return True

# Define roles and their permissions
roles = {
    "adult premium": Role("adult premium", [Permission("R", "new"), Permission("R", "old"), Permission("PG-13", "new"), Permission("PG-13", "old"), Permission("G", "new"), Permission("G", "old")]),
    "adult regular": Role("adult regular", [Permission("R", "old"), Permission("PG-13", "old"), Permission("G", "old")]),
    "teenage premium": Role("teenage premium", [Permission("PG-13", "new"), Permission("PG-13", "old"), Permission("G", "new"), Permission("G", "old")]),
    "teenage regular": Role("teenage regular", [Permission("PG-13", "old"), Permission("G", "old")]),
    "child premium": Role("child premium", [Permission("G", "new"), Permission("G", "old")]),
    "child regular": Role("child regular", [Permission("G", "old")])
}

# Check if a user can access a movie
def can_user_access_movie(user, movie_rating, release_type):
    user_role = roles[user.role]
    for permission in user_role.permissions:
        if permission.movie_rating == movie_rating and permission.release_type == release_type:
            return permission.can_access(user.role)
    return False

# Example usage:
user1 = User("Qu", "adult premium")
print("Checking Qu's permissions:")
print(can_user_access_movie(user1, "R", "new"))  
print(can_user_access_movie(user1, "PG-13", "old")) 
print(can_user_access_movie(user1, "G", "new"))  

print("\n")

user2 = User("Tyler", "child regular")
print("Checking Tyler's permissions:")
print(can_user_access_movie(user2, "R", "new"))
print(can_user_access_movie(user2, "PG-13", "old"))
print(can_user_access_movie(user2, "G", "new")) 

print("\n")

user3 = User("Dan", "teenage premium")
print("Checking Dan's permissions:")
print(can_user_access_movie(user3, "R", "new"))
print(can_user_access_movie(user3, "PG-13", "old"))
print(can_user_access_movie(user3, "G", "new"))


