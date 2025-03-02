# Store Billing System

## Overview
This is a simple Python program that simulates a store billing system. It allows users to enter item codes, prices, and quantities to calculate the total bill.

## Features
- Allows dynamic input for the number of items.
- Accepts item codes and their respective prices.
- Displays the list of items with their prices.
- Prompts the user to enter quantities for each item.
- Computes and displays the total bill.

## Requirements
- Python 3.x installed

## Installation
1. Clone this repository using:
   ```sh
   git clone https://github.com/aniketmondal1210/store-billing-system.git
2. Navigate to the project directory:
   cd store-billing-system
3. Run the script using:
   python store_billing.py

Usage

  1. Run the Python script.
  2. Enter the number of items.
  3. Input the item codes and their respective prices.
  4. Enter the quantity of each item.
  5. View the calculated bill.

Example Output
Enter the number of items: 3
Enter the code of item 1: 101
Enter the price of item 1: 50
Enter the code of item 2: 102
Enter the price of item 2: 30
Enter the code of item 3: 103
Enter the price of item 3: 20

ITEM CODE      PRICE
-------------------
101           50
102           30
103           20

Enter the quantity for each item:
Quantity for item 101: 2
Quantity for item 102: 3
Quantity for item 103: 1

************ BILL ************
------------------------------
ITEM CODE    PRICE    QUANTITY    SUBTOTAL
------------------------------------------
101         50         2         100
102         30         3         90
103         20         1         20
------------------------------------------
Total Bill Amount: ₹210
****************************

Future Enhancements

1. Add a database to store item details.
2. Implement a GUI version using Tkinter or PyQt.
3. Allow users to apply discounts and taxes.
4. Generate invoice PDFs for the bill.

Contributing

Contributions are welcome! Follow these steps to contribute:

  1. Fork the repository.
  2. Create a new branch:
    git checkout -b feature-branch
  3. Make your changes and commit:
     git commit -m "Added a new feature"
  4. Push to your forked repo:
     git push origin feature-branch
  5. Open a Pull Request.


Author - https://github.com/aniketmondal1210 

License
  This project is open-source and free to use.
  
Let me know if you need any modifications! 🚀
