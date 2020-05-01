# A class is like a blueprint for creating objects. An object has properties and methods(functions) associated with it. Almost everything in Python is an object

# Create class
class User:
    # Constructor
    def __init__(self, name, email, age):
        self.name = name
        self.email = email
        self.age = age

    def greeting(self):
        return f'My name is {self.name} and I am {self.age}'

    def has_birthday(self):
        self.age += 1

# Customer class
class Customer(User):
    def __super__(self, name, email, age):
        self.name = name
        self.email = email
        self.age = age
        self.balance = 0

    def set_balance(self, balance):
        self.balance = balance

    def greeting(self):
        return f'My name is {self.name} and I am {self.age} and I owe balance {self.balance}'


# Init user object
fikar = User('Fikar', 'dzulfikar.maulana@gmail.com', 20)
janet = User('Janet', 'janet@gmail.com', 25)

# Edit Property
fikar.age = 40

janet.has_birthday()

# Call method
# print(janet.greeting())

# Init customer
john = Customer('John Doe', 'john@gmail.com', 45)

john.set_balance(400)

print(john.greeting())