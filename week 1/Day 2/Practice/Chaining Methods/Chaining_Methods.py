class User:
    def __init__(self, first_name,last_name,email,age ):
        self.name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age
        self.is_rewards_member = False
        self.gold_card_points = 0

    def display_info(self):
        print("==================================")
        print(f"First Name: {self.name}")
        print(f"Last Name: {self.last_name}")
        print(f"Email: {self.email}")
        print(f"Age: {self.age}")
        print(f"Rewards Member: {self.is_rewards_member}")
        print(f"Gold Card Points: {self.gold_card_points}")
        print("==================================")
        return self

    def enroll(self):
        self.is_rewards_member = False
        self.gold_card_points = 200
        return self

    def spend_points(self, amount):
        self.gold_card_points -= amount
        return self


# user 1
user1=User("mohamed","cherif","cherif@gmail.com",22)
user1.display_info().enroll().spend_points(50).display_info().enroll()

# user 2
user2=User("ayoub","mejri","ayoub21@gmail.com",27)
user2.enroll().spend_points(80).display_info()

# user 3
user3=User("sirine","amry","sisimomi@gmail.com",20)
user3.display_info().spend_points(40)




