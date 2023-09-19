#!/usr/bin/env python
# coding: utf-8

# # 1

# In[7]:


import math

class Shape:
    def __init__(self):
        pass

    def area(self):
        pass

    def perimeter(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        super().__init__()
        self.rad = radius

    def area(self):
        return math.pi * self.rad**2

    def perimeter(self):
        return 2 * math.pi * self.rad

class Rectangle(Shape):
    def __init__(self, length, width):
        super().__init__()
        self.len = length
        self.wid = width

    def area(self):
        return self.len * self.wid

    def perimeter(self):
        return 2 * (self.len + self.wid)

cs = Circle(7)
rs = Rectangle(4, 6)

print("Area of circle:", cs.area())
print("Perimeter of circle:", cs.perimeter())

print("Area of Rectangle:", rs.area())
print("Perimeter of Rectangle:", rs.perimeter())


# # 2

python
class Person:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def get_age(self):
        return self.__age

    def is_eligible_to_vote(self):
        if self.__age >= 18:
            return True
        else:
            return False

# Example usage:
person1 = Person("John", 25)
print(f"{person1.get_age()}-year-old {person1._Person__name} is eligible to vote: {person1.is_eligible_to_vote()}")

person2 = Person("Alice", 16)
print(f"{person2.get_age()}-year-old {person2._Person__name} is eligible to vote: {person2.is_eligible_to_vote()}")


# # 3

# In[10]:


class BankAccount:
    def __init__(self, account_number, account_holder_name, balance):
        self.account_number = account_number
        self.account_holder_name = account_holder_name
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return True
        else:
            return False

    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            return True
        else:
            return False

class SavingsAccount(BankAccount):
    def __init__(self, account_number, account_holder_name, balance, interest_rate):
        super().__init__(account_number, account_holder_name, balance)
        self.interest_rate = interest_rate

    def calculate_interest(self):
        interest = (self.balance * self.interest_rate) / 100
        self.balance += interest
        return interest

class CheckingAccount(BankAccount):
    def __init__(self, account_number, account_holder_name, balance, overdraft_limit):
        super().__init__(account_number, account_holder_name, balance)
        self.overdraft_limit = overdraft_limit

    def withdraw(self, amount):
        if amount > 0 and amount <= (self.balance + self.overdraft_limit):
            self.balance -= amount
            return True
        else:
            return False


savings_account = SavingsAccount("ab56789", "siva", 5000, 2.5)
checking_account = CheckingAccount("Cd67890", "punith", 3000, 1000)

print(f"Savings Account - Holder: {savings_account.account_holder_name}, Balance: {savings_account.balance}")
print(f"Checking Account - Holder: {checking_account.account_holder_name}, Balance: {checking_account.balance}")

savings_account.deposit(7000)
checking_account.deposit(5000)

print(f"Savings Account - New Balance: {savings_account.balance}")
print(f"Checking Account - New Balance: {checking_account.balance}")

savings_interest = savings_account.calculate_interest()
print(f"Savings Account - Interest Earned: {savings_interest}, New Balance: {savings_account.balance}")

savings_account.withdraw(2000)
checking_account.withdraw(4000)

print(f"Savings Account - New Balance after withdrawal: {savings_account.balance}")
print(f"Checking Account - New Balance after withdrawal: {checking_account.balance}")


# # 4

# In[12]:


class Employee:
    def __init__(self, name, emp_id, salary):
        self.__name = name
        self.__emp_id = emp_id
        self.__salary = salary

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_emp_id(self):
        return self.__emp_id

    def set_emp_id(self, emp_id):
        self.__emp_id = emp_id

    def get_salary(self):
        return self.__salary

    def set_salary(self, salary):
        self.__salary = salary

    def calculate_salary(self):
        pass

class FullTimeEmployee(Employee):
    def __init__(self, name, emp_id, annual_salary):
        super().__init__(name, emp_id, annual_salary)
        self.__annual_salary = annual_salary

    def calculate_salary(self):
        return self.__annual_salary

class PartTimeEmployee(Employee):
    def __init__(self, name, emp_id, hourly_rate, hours_worked):
        super().__init__(name, emp_id, hourly_rate)  
        self.__hourly_rate = hourly_rate
        self.__hours_worked = hours_worked

    def calculate_salary(self):
        return self.__hourly_rate * self.__hours_worked

full_time_emp = FullTimeEmployee("John Doe", "FT001", 60000)
part_time_emp = PartTimeEmployee("Jane Smith", "PT001", 20, 25)

print(f"{full_time_emp.get_name()} (Employee ID: {full_time_emp.get_emp_id()})")
print(f"Annual Salary: ${full_time_emp.calculate_salary()}\n")

print(f"{part_time_emp.get_name()} (Employee ID: {part_time_emp.get_emp_id()})")
print(f"Hourly Rate: ${part_time_emp.get_salary()}")
print(f"Hours Worked: {part_time_emp.calculate_salary() / part_time_emp.get_salary()}")
print(f"Monthly Salary: ${part_time_emp.calculate_salary()}")


# # 5

class Book:
    def __init__(self, title, author, publication_date, book_type):
        self.title = title
        self.author = author
        self.publication_date = publication_date
        self.book_type = book_type
        self.checked_out = False
        self.checkout_date = None

    def is_available(self):
        return not self.checked_out

    def checkout(self):
        if self.is_available():
            self.checked_out = True
            self.checkout_date = datetime.now()
            print(f"Checked out: {self.title}")
        else:
            print(f"{self.title} is already checked out.")

    def return_book(self):
        if not self.is_available():
            days_checked_out = (datetime.now() - self.checkout_date).days
            if days_checked_out > 14:
                print(f"Late return! You owe a fee for {days_checked_out - 14} days.")
            self.checked_out = False
            self.checkout_date = None
            print(f"Returned: {self.title}")
        else:
            print(f"{self.title} is already available.")

class Patron:
    def __init__(self, name, id):
        self.name = name
        self.id = id
        self.checked_out_books = []

    def check_out_book(self, book):
        if book.is_available():
            self.checked_out_books.append(book)
            book.checkout()
        else:
            print(f"{book.title} is not available for checkout.")

    def return_book(self, book):
        if book in self.checked_out_books:
            self.checked_out_books.remove(book)
            book.return_book()
        else:
            print(f"You didn't check out {book.title}.")

def main():
    book1 = Book("The Great Gatsby", "F. Scott Fitzgerald", "1925", "Fiction")
    book2 = Book("To Kill a Mockingbird", "Harper Lee", "1960", "Fiction")
    book3 = Book("The Elements of Style", "William Strunk Jr.", "1918", "Non-Fiction")

    patron1 = Patron("Alice", 101)
    patron2 = Patron("Bob", 102)

    patron1.check_out_book(book1)
    patron2.check_out_book(book2)

    book1.return_book()
    patron2.return_book(book2)

if __name__ == "__main__":
    main()

# # 6
python
class Product:
    def __init__(self, product_id, name, price):
        self.__product_id = product_id
        self.__name = name
        self.__price = price

    def get_product_id(self):
        return self.__product_id

    def get_name(self):
        return self.__name

    def get_price(self):
        return self.__price

    def calculate_discount(self, discount_percentage):
        return self.__price * (1 - discount_percentage / 100)

class Electronic(Product):
    def __init__(self, product_id, name, price, brand):
        super().__init__(product_id, name, price)
        self.__brand = brand

    def get_brand(self):
        return self.__brand

class Clothing(Product):
    def __init__(self, product_id, name, price, size):
        super().__init__(product_id, name, price)
        self.__size = size

    def get_size(self):
        return self.__size

class ShoppingCart:
    def __init__(self):
        self.__items = []

    def add_item(self, product, quantity):
        self.__items.append({"product": product, "quantity": quantity})

    def remove_item(self, product):
        self.__items = [item for item in self.__items if item["product"] != product]

    def calculate_total_cost(self):
        total_cost = 0
        for item in self.__items:
            total_cost += item["product"].get_price() * item["quantity"]
        return total_cost

class Order:
    def __init__(self, order_id, items, shipping_cost):
        self.__order_id = order_id
        self.__items = items
        self.__shipping_cost = shipping_cost

    def get_order_id(self):
        return self.__order_id

    def calculate_total_cost(self):
        total_cost = 0
        for item in self.__items:
            total_cost += item["product"].get_price() * item["quantity"]
        total_cost += self.__shipping_cost
        return total_cost

# Example usage:
# Create products
tv = Electronic(1, "Smart TV", 500, "Samsung")
shirt = Clothing(2, "Casual Shirt", 30, "Medium")

# Create a shopping cart
cart = ShoppingCart()
cart.add_item(tv, 2)
cart.add_item(shirt, 5)

# Calculate the total cost in the shopping cart
cart_total = cart.calculate_total_cost()
print(f"Shopping Cart Total Cost: ${cart_total}")

# Place an order
order = Order(101, cart._ShoppingCart__items, 10)  # Shipping cost is $10
order_total = order.calculate_total_cost()
print(f"Order Total Cost: ${order_total}")