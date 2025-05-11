class ItemToPurchase:
    def __init__(self, name="none", desc="none", price=0.0, qty=0):
        self.name, self.description, self.price, self.quantity = name, desc, price, qty

    def print_item_cost(self):
        print(f"{self.name} {self.quantity} @ ${self.price:.0f} = ${self.price * self.quantity:.0f}")


class ShoppingCart:
    def __init__(self, customer="none", date="January 1, 2020"):
        self.customer_name, self.current_date, self.cart_items = customer, date, []

    def add_item(self, item): self.cart_items.append(item)

    def remove_item(self, name):
        if name not in [i.name for i in self.cart_items]:
            print("Item not found in cart. Nothing removed.")
        self.cart_items = [i for i in self.cart_items if i.name != name]

    def modify_item(self, item):
        for i in self.cart_items:
            if i.name == item.name:
                if item.description != "none": i.description = item.description
                if item.price: i.price = item.price
                if item.quantity: i.quantity = item.quantity
                return
        print("Item not found in cart. Nothing modified.")

    def get_num_items_in_cart(self): return sum(i.quantity for i in self.cart_items)

    def get_cost_of_cart(self):
        return sum(i.price * i.quantity for i in self.cart_items)

    def print_total(self):
        print(f"\nOUTPUT SHOPPING CART\n{self.customer_name}'s Shopping Cart - {self.current_date}")
        print(f"Number of Items: {self.get_num_items_in_cart()}")
        if not self.cart_items:
            print("SHOPPING CART IS EMPTY")
        else:
            for i in self.cart_items:
                i.print_item_cost()
        print(f"\nTotal: ${self.get_cost_of_cart():.0f}")

    def print_descriptions(self):
        print(f"\nOUTPUT ITEMS' DESCRIPTIONS\n{self.customer_name}'s Shopping Cart - {self.current_date}")
        for i in self.cart_items:
            print(f"{i.name}: {i.description}")


def print_menu(cart):
    while True:
        print("\nMENU\na - Add item to cart\n"
              "r - Remove item from cart\n"
              "c - Change item quantity\n"
              "i - Output items' descriptions\n"
              "o - Output shopping cart\n"
              "q - Quit")
        choice = input("Choose an option: ").lower()

        if choice == 'a':
            try:
                name = input("Enter the item name: ")
                desc = input("Enter the item description: ")
                price = float(input("Enter the item price: "))
                qty = int(input("Enter the item quantity: "))
                cart.add_item(ItemToPurchase(name, desc, price, qty))
            except ValueError:
                print("Invalid input. Price must be a number and quantity must be a whole number.")

        elif choice == 'r':
            name = input("Enter name of item to remove: ")
            cart.remove_item(name)

        elif choice == 'c':
            try:
                name = input("Enter the item name: ")
                qty = int(input("Enter the new quantity: "))
                cart.modify_item(ItemToPurchase(name, "none", 0.0, qty))  # ✅ FIXED
            except ValueError:
                print("Invalid input. Quantity must be a whole number.")

        elif choice == 'i':
            cart.print_descriptions()

        elif choice == 'o':
            cart.print_total()

        elif choice == 'q':
            break

        else:
            print("Invalid option. Please choose a valid menu option.")


def main():
    print("Item 1")
    try:
        name1 = input("Enter the item name:\n")
        price1 = float(input("Enter the item price:\n"))
        qty1 = int(input("Enter the item quantity:\n"))
        i1 = ItemToPurchase(name1, "none", price1, qty1)
    except ValueError:
        print("Invalid input. Price must be a number and quantity must be a whole number.")
        return

    print("\nItem 2")
    try:
        name2 = input("Enter the item name:\n")
        price2 = float(input("Enter the item price:\n"))
        qty2 = int(input("Enter the item quantity:\n"))
        i2 = ItemToPurchase(name2, "none", price2, qty2)
    except ValueError:
        print("Invalid input. Price must be a number and quantity must be a whole number.")
        return

    print("\nTOTAL COST")
    i1.print_item_cost()
    i2.print_item_cost()
    total = i1.price * i1.quantity + i2.price * i2.quantity
    print(f"Total: ${total:.0f}")

    name = input("\nEnter customer name:\n")
    date = input("Enter date:\n")
    print(f"\nCustomer name: {name}\nToday's date: {date}")

    cart = ShoppingCart(name, date)
    print_menu(cart)


if __name__ == "__main__":
    main()
