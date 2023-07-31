class Cart:
    def __init__(self):
        self.cart_items = []

    def show_cart(self):
        print("Current Shopping List:")
        for item in self.cart_items:
            print(item)
        print()

    def add_item(self):
        item = input("Enter the name of the item you want to add: ")
        self.cart_items.append(item)
        print(f"{item} added to the shopping cart.\n")

    def delete_item(self):
        item = input("Enter the name of the item you want to delete: ")
        if item in self.cart_items:
            self.cart_items.remove(item)
            print(f"{item} removed from the shopping cart.\n")
        else:
            print(f"{item} not found in the shopping cart.\n")

    def shopping_cart(self):
        while True:
            action = input("Do you want to: show/add/delete or quit? ").lower()

            if action == 'show':
                self.show_cart()
            elif action == 'add':
                self.add_item()
            elif action == 'delete':
                self.delete_item()
            elif action == 'quit':
                print("Final Shopping List:")
                self.show_cart()
                break
            else:
                print("Invalid input. Please try again.\n")

my_cart = Cart()

my_cart.shopping_cart()