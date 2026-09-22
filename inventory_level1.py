"""
=====================================================================
 INVENTORY STOCK ANALYSIS SYSTEM  -  LEVEL 1  (UTILITY 1)
 Module 1 : Fundamentals of Python Programming / Control Structures
---------------------------------------------------------------------
 Name : Shrushti Nandkishor Dhawad | USN : ME25TCD002 | CSE-DS (B)
 Course : Python Programming Lab (N-PCCCD304P)
---------------------------------------------------------------------
 AIM : To develop the FIRST stage of an Inventory Management System
       that uses arrays (Python lists) to track the stock level of a
       fixed set of items, records every sale, and raises a
       restocking alert whenever an item's quantity falls below a
       safety threshold.

 CONCEPTS USED (Module 1 only) :
   - Variables and data types (int, str, bool)
   - Input / output statements
   - Arithmetic and relational operators
   - Decision making  : if / elif / else
   - Looping          : while loop, for loop
   - Loop control     : break, continue
   - A simple array (list) used only for storage and indexing --
     no functions and no list methods beyond indexing are used
     here, everything is written as plain, easy, step-by-step code.
=====================================================================
"""

# ------------------------- CONSTANTS / "ARRAYS" ----------------------
# Two parallel arrays : item names and their matching stock levels.
ITEM_NAMES = ["Rice", "Wheat", "Sugar", "Salt", "Cooking Oil"]
stock_levels = [50, 30, 20, 15, 10]          # array of current stock
TOTAL_ITEMS = len(ITEM_NAMES)                # number of items tracked
RESTOCK_THRESHOLD = 10                       # alert trigger level


# ------------------------- 1. WELCOME --------------------------------
print("=" * 60)
print("        INVENTORY STOCK ANALYSIS SYSTEM  -  LEVEL 1")
print("=" * 60)
print("This program tracks stock levels, records sales and shows")
print("restocking alerts for", TOTAL_ITEMS, "items using simple arrays.")
print()

manager_name = input("Enter store manager's name : ")

if manager_name == "":                        # decision making
    manager_name = "Manager"

print("Welcome,", manager_name, "! Let us manage the inventory.")
print("-" * 60)


# ------------------------- 2. MAIN MENU LOOP ---------------------------
total_sold_units = 0        # accumulator variable
total_restocked_units = 0   # accumulator variable
sales_count = 0              # counter variable
alerts_raised = 0            # counter variable

running = True               # boolean flag that controls the while loop

while running:                                       # WHILE LOOP
    print("\nMENU : [1] View Stock  [2] Sell Item  [3] Restock Item"
          "  [4] Exit")
    choice = input("Enter your choice (1-4) : ").strip()

    # ---- simple validation using decision making ----
    if choice.isdigit() == False:
        print(">> Please type a NUMBER only. Try again.")
        continue                                     # CONTINUE statement

    choice = int(choice)                             # type conversion

    if choice < 1 or choice > 4:
        print(">> Value must be between 1 and 4. Try again.")
        continue

    # ---------------------- OPTION 1 : VIEW STOCK ----------------------
    if choice == 1:
        print("\n" + " CURRENT STOCK ".center(60, "="))
        print("%-4s %-15s %-10s %-s" % ("No", "Item", "Stock", "Status"))
        for i in range(TOTAL_ITEMS):                       # FOR LOOP
            if stock_levels[i] <= RESTOCK_THRESHOLD:        # decision making
                status = "!! LOW - RESTOCK ALERT !!"
            else:
                status = "OK"
            print("%-4d %-15s %-10d %-s" % (i + 1, ITEM_NAMES[i],
                                             stock_levels[i], status))
        print("=" * 60)

    # ---------------------- OPTION 2 : SELL ITEM ------------------------
    elif choice == 2:
        print("\n" + " CURRENT STOCK ".center(60, "="))
        print("%-4s %-15s %-10s %-s" % ("No", "Item", "Stock", "Status"))
        for i in range(TOTAL_ITEMS):
            if stock_levels[i] <= RESTOCK_THRESHOLD:
                status = "!! LOW - RESTOCK ALERT !!"
            else:
                status = "OK"
            print("%-4d %-15s %-10d %-s" % (i + 1, ITEM_NAMES[i],
                                             stock_levels[i], status))
        print("=" * 60)

        idx = input("Enter item number to sell (1-%d) : " % TOTAL_ITEMS)

        if idx.isdigit() == False or int(idx) < 1 or int(idx) > TOTAL_ITEMS:
            print(">> Invalid item number.")
            continue

        idx = int(idx) - 1                            # convert to array index

        qty = input("Enter quantity to sell : ")
        if qty.isdigit() == False or int(qty) <= 0:
            print(">> Please enter a positive whole number.")
            continue
        qty = int(qty)

        # ---- relational / arithmetic operators ----
        if qty > stock_levels[idx]:
            print("  Result : INSUFFICIENT STOCK ! Only",
                  stock_levels[idx], "units available.")
        else:
            stock_levels[idx] = stock_levels[idx] - qty   # update the array
            total_sold_units = total_sold_units + qty
            sales_count = sales_count + 1
            print("  Sold", qty, "units of", ITEM_NAMES[idx],
                  " | Remaining stock :", stock_levels[idx])

            # ---- restocking alert (if / elif / else) ----
            if stock_levels[idx] == 0:
                print("  ALERT : OUT OF STOCK for", ITEM_NAMES[idx], "!")
                alerts_raised = alerts_raised + 1
            elif stock_levels[idx] <= RESTOCK_THRESHOLD:
                print("  ALERT : LOW STOCK for", ITEM_NAMES[idx],
                      "-> please restock soon.")
                alerts_raised = alerts_raised + 1

    # ---------------------- OPTION 3 : RESTOCK ITEM ----------------------
    elif choice == 3:
        print("\n" + " CURRENT STOCK ".center(60, "="))
        print("%-4s %-15s %-10s %-s" % ("No", "Item", "Stock", "Status"))
        for i in range(TOTAL_ITEMS):
            if stock_levels[i] <= RESTOCK_THRESHOLD:
                status = "!! LOW - RESTOCK ALERT !!"
            else:
                status = "OK"
            print("%-4d %-15s %-10d %-s" % (i + 1, ITEM_NAMES[i],
                                             stock_levels[i], status))
        print("=" * 60)

        idx = input("Enter item number to restock (1-%d) : " % TOTAL_ITEMS)

        if idx.isdigit() == False or int(idx) < 1 or int(idx) > TOTAL_ITEMS:
            print(">> Invalid item number.")
            continue

        idx = int(idx) - 1

        qty = input("Enter quantity to add : ")
        if qty.isdigit() == False or int(qty) <= 0:
            print(">> Please enter a positive whole number.")
            continue
        qty = int(qty)

        stock_levels[idx] = stock_levels[idx] + qty        # update the array
        total_restocked_units = total_restocked_units + qty
        print("  Restocked", qty, "units of", ITEM_NAMES[idx],
              " | New stock :", stock_levels[idx])

    # ---------------------- OPTION 4 : EXIT -------------------------------
    else:
        running = False                                 # stop the while loop
        break                                            # BREAK statement


# ------------------------- 3. FINAL SUMMARY ---------------------------
print()
print("=" * 60)
print("                 SESSION SUMMARY")
print("=" * 60)
print("Manager Name           :", manager_name)
print("Total Sales Made       :", sales_count)
print("Total Units Sold       :", total_sold_units)
print("Total Units Restocked  :", total_restocked_units)
print("Restock Alerts Raised  :", alerts_raised)

# ---- find item with the highest current stock (loop-based "max") ----
highest_stock = stock_levels[0]
highest_item = ITEM_NAMES[0]
for i in range(1, TOTAL_ITEMS):
    if stock_levels[i] > highest_stock:
        highest_stock = stock_levels[i]
        highest_item = ITEM_NAMES[i]

print("Item with Highest Stock:", highest_item, "(", highest_stock, "units )")

print("\n" + " FINAL STOCK ".center(60, "="))
print("%-4s %-15s %-10s %-s" % ("No", "Item", "Stock", "Status"))
for i in range(TOTAL_ITEMS):
    if stock_levels[i] <= RESTOCK_THRESHOLD:
        status = "!! LOW - RESTOCK ALERT !!"
    else:
        status = "OK"
    print("%-4d %-15s %-10d %-s" % (i + 1, ITEM_NAMES[i],
                                     stock_levels[i], status))
print("=" * 60)

print("Thank you for using the Inventory Stock Analysis System,",
      manager_name, "!")
