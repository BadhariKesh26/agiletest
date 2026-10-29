def calculate_bill():
    print("\n--- Shopping Bill Calculator ---")
    try:
        price = float(input("Enter item price: "))
        quantity = int(input("Enter item quantity: "))
        
        
        total = price * quantity
        print(f"Subtotal: ${total:.2f}")
        
        
        if total > 100:
            discount = total * 0.10
            total -= discount
            print(f"Discount (10%): -${discount:.2f}")
            
        print(f"Total Bill: ${total:.2f}")
    except ValueError:
        print("Invalid input. Please enter numbers only.")

def menu():
    while True:
        print("\n1. Calculate New Bill")
        print("2. Exit")
        choice = input("Choose an option: ")
        if choice == '1':
            calculate_bill()
        elif choice == '2':
            print("Exiting application.")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    menu()