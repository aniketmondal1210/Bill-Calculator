class Store:
    def __init__(self):
        self.item_code = []
        self.price = []
        self.n = int(input("Enter the number of items: "))  # Allowing dynamic input

    def get_data(self):
        for i in range(self.n):
            code = int(input(f"Enter the code of item {i+1}: "))
            price = int(input(f"Enter the price of item {i+1}: "))
            self.item_code.append(code)
            self.price.append(price)

    def display_data(self):
        print("\nITEM CODE\tPRICE")
        print("-" * 25)
        for i in range(self.n):
            print(self.item_code[i], "\t\t", self.price[i])

    def calculate_bill(self):
        total_amount = 0
        quantities = []
        
        print("\nEnter the quantity for each item:")
        for i in range(self.n):
            qty = int(input(f"Quantity for item {self.item_code[i]}: "))
            quantities.append(qty)
            total_amount += self.price[i] * qty

        print("\n************ BILL ************")
        print("ITEM CODE\tPRICE\tQUANTITY\tSUBTOTAL")
        print("-" * 40)
        for i in range(self.n):
            subtotal = self.price[i] * quantities[i]
            print(self.item_code[i], "\t\t", self.price[i], "\t", quantities[i], "\t\t", subtotal)
        print("-" * 40)
        print(f"Total Bill Amount: ₹{total_amount}")
        print("****************************")


# Creating Store object and running methods
s = Store()
s.get_data()
s.display_data()
s.calculate_bill()
