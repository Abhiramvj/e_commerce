from design import Product
    def reduce_stock(self, quantity):
        if self.stock >= quantity:
            self.stock -= quantity
            print(f"Sold {quantity} units of {self.name}. Remaining stock: {self.stock}")
            if self.stock < 10:
                print(f"Alert: Stock for {self.name} is below 10 units! Please consider restocking.")
        else:
            print(f"Error: Not enough stock for {self.name}. Available: {self.stock}, Requested: {quantity}")

    def restock(self, quantity):
        self.stock += quantity
        print(f"Restocked {quantity} units of {self.name}. New stock: {self.stock}")


products = [
    Product(1, "Laptop", 1500, 25),    # Initial stock is 25
    Product(2, "Phone", 800, 50),      # Initial stock is 50
    Product(3, "Headphones", 100, 30), # Initial stock is 30
]

def find_product_by_id(product_id):
    for product in products:
        if product.product_id == product_id:
            return product
    print(f"Product with ID {product_id} not found!")
    return None

def sell_product():
    while True:
        try:
            product_id = int(input("Enter product ID to sell (or 0 to stop): "))
            if product_id == 0:
                break
            product = find_product_by_id(product_id)
            if product:
                quantity = int(input(f"Enter quantity to sell for {product.name}: "))
                product.reduce_stock(quantity)
                if product.stock < 10:
                    restock_quantity = int(input(f"Do you want to restock {product.name}? Enter quantity (or 0 to skip): "))
                    if restock_quantity > 0:
                        product.restock(restock_quantity)
        except ValueError:
            print("Invalid input! Please enter valid numbers.")

def display_products():
    print("\nAvailable products:")
    for product in products:
        print(f"ID: {product.product_id}, Name: {product.name}, Price: ${product.price}, Stock: {product.stock}")
    print("\n")

if __name__ == "__main__":
    while True:
        display_products()
        sell_product()
        stop = input("Do you want to continue? (yes to continue, no to stop): ").lower()
        if stop == 'no':
            break

