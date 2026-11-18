
print("  ******welcome to jaibiru resurant management system ******")

print("\n------ MENU ------")
print("1. Pizza       - Rs.150")
print("2. Burger      - Rs.80")
print("3. Momos       - Rs.60")
print("4. Cold Drink  - Rs.40")
print("5. French Fries- Rs.70")
print("6. biryani       - 130")
print("7.samosa   - Rs.15")
print("----------------------------")
total = 0

while True:
    choice = int(input("\nEnter item number (0 to finish): "))

    if choice == 0:
        break

    if choice == 1:
        price = 150
        item = "Pizza"

    elif choice == 2:
        price = 80
        item = "Burger"

    elif choice == 3:
        price = 60
        item = "Momos"

    elif choice == 4:
        price = 40
        item = "Cold Drink"

    elif choice == 5:
        price = 70
        item = "French Fries"
        
    elif choice ==6:
        price = 130
        item ="biryani"
        
    elif choice ==7:
        price =15
        item ="samosa"

    else:
        print("Invalid choice!")
        continue

    quantity = int(input("Enter quantity: "))

    amount = price * quantity
    total = total + amount

    print(item, "added =", amount, "Rs.")

print("\n================================")
print("           FINAL BILL")
print("================================")
print("Total Bill =", total, "Rs.")
print("Thank you for visiting!")
print("================================")