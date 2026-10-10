

print("Welcome to Restaurant Bill Calculator!")

while True:
    # 1. User Inputs (Variables & Type Casting)
    try:
        people = int(input("Enter number of people: "))
        
        # Validation: If number of people is <= 0, ask again
        while people <= 0:
            print("Error: Number of people must be greater than 0.")
            people = int(input("Enter number of people again: "))

        bill = float(input("Enter total bill amount: Rs. "))

        # Validation: If bill amount is negative
        if bill < 0:
            print("Error: Bill amount cannot be negative.")
            continue # restart the loop

        tip_percent = int(input("Enter tip percentage (0, 5, 10, 15, 20): "))

        # Validation: If tip percentage is negative
        if tip_percent < 0:
            print("Error: Tip percentage cannot be negative.")
            continue

        # Optional: Check if tip is from allowed list
        allowed_tips = [0, 5, 10, 15, 20]
        if tip_percent not in allowed_tips:
            print(f"Warning: You entered {tip_percent}%, but recommended is {allowed_tips}")

        # 2. Calculations (Operators & Expressions)
        tip_amount = (tip_percent / 100) * bill
        final_bill = bill + tip_amount
        per_person = final_bill / people

        # 3. Display all values properly formatted
        print("\n--------- Bill Summary ---------")
        print(f"Total Bill      : Rs. {bill:.2f}")
        print(f"Tip Percentage  : {tip_percent}%")
        print(f"Tip Amount      : Rs. {tip_amount:.2f}")
        print(f"Final Bill      : Rs. {final_bill:.2f}")
        print(f"Number of People: {people}")
        print(f"Each Person Pays: Rs. {per_person:.2f}")
        print("--------------------------------\n")

        # 4. Optional Looping Task - Ask for another calculation
        choice = input("Do you want to calculate another bill? (yes/no): ").lower()
        if choice != 'yes' and choice != 'y':
            print("Thank you! Visit again.")
            break

    except ValueError:
        print("Error: Please enter valid numbers only.\n")