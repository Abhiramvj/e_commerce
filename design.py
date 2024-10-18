class Product:
    def __init__(self, product_id, name, price, stock):
        self.product_id = product_id
        self.name = name
        self.price = price
        self.stock = stock

    def reduce_stock(self, quantity):
        if self.stock >= quantity:
            self.stock -= quantity
            return True
        else:
            print(f"Error: Not enough stock for {self.name}. Available: {self.stock}, Requested: {quantity}")
            return False

    def restock(self, quantity):
        self.stock += quantity
        print(f"Restocked {quantity} units of {self.name}. New stock: {self.stock}")

class Order:
    def __init__(self, order_id, user):
        self.order_id = order_id
        self.user = user
        self.products = []  
        self.status = "Pending"  

    def add_product(self, product, quantity):
        if product.reduce_stock(quantity):  
            self.products.append((product, quantity))
            print(f"Added {quantity} of {product.name} to order {self.order_id}.")
        else:
            print(f"Cannot add {product.name} to order {self.order_id} due to insufficient stock.")

    def complete_payment(self, payment):
        total_cost = sum(product.price * quantity for product, quantity in self.products)
        if total_cost == payment.amount:
            self.status = "Completed"
            print(f"Payment successful for order {self.order_id}. Status updated to {self.status}.")
            return True  
        else:
            print(f"Payment failed for order {self.order_id}. Expected: ${total_cost}, Provided: ${payment.amount}.")
            return False  

    def ship_order(self):
        if self.status == "Completed":
            self.status = "Shipped"
            print(f"Order {self.order_id} has been shipped.")
        else:
            print(f"Order {self.order_id} cannot be shipped because it's not completed.")

class User:
    def __init__(self, user_id, name):
        self.user_id = user_id
        self.name = name
        self.orders = []  
    def create_order(self, order_id):
        order = Order(order_id, self)
        self.orders.append(order)
        return order

products = [
    Product(1, "Laptop", 1500, 25),    
    Product(2, "Phone", 800, 50),      
    Product(3, "Headphones", 100, 30), 
]


users = [
    User(1, "Alice"),
    User(2, "Bob"),
    User(3, "Charlie"),
]

def find_product_by_id(product_id):
    for product in products:
        if product.product_id == product_id:
            return product
    print(f"Product with ID {product_id} not found!")
    return None

def display_products():
    print("\nAvailable products:")
    for product in products:
        print(f"ID: {product.product_id}, Name: {product.name}, Price: ${product.price}, Stock: {product.stock}")
    print("\n")

def manage_orders(user):
    while True:
        print(f"\nManaging orders for {user.name}.")
        action = input("Choose action - Create Order (1), View Orders (2), Exit (3): ")
        if action == '1':
            order_id = len(user.orders) + 1 
            order = user.create_order(order_id)
            while True:
                display_products()
                product_id = int(input("Enter product ID to add to the order (or 0 to finish): "))
                if product_id == 0:
                    break
                product = find_product_by_id(product_id)
                if product:
                    quantity = int(input(f"Enter quantity to add for {product.name}: "))
                    order.add_product(product, quantity)
            payment_amount = int(input("Enter payment amount for the order: "))
            order.complete_payment(Payment(payment_amount))  

        elif action == '2':
            print(f"\nOrders for {user.name}:")
            for order in user.orders:
                print(f"Order ID: {order.order_id}, Status: {order.status}")
                for product, quantity in order.products:
                    print(f"  {product.name} x {quantity}")
            print("\n")
        
        elif action == '3':
            break

        else:
            print("Invalid option! Please choose again.")

class Payment:
    def __init__(self, amount):
        self.amount = amount

if __name__ == "__main__":
    while True:
        print("\nSelect a user:")
        for user in users:
            print(f"{user.user_id}: {user.name}")
        user_id = int(input("Enter user ID (or 0 to exit): "))
        if user_id == 0:
            break
        selected_user = next((user for user in users if user.user_id == user_id), None)
        if selected_user:
            manage_orders(selected_user)
        else:
            print("User not found! Please try again.")
