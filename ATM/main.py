# balance = 5,000


# while True:
#     print("\n==================")
#     print("    WELCOME TO GOLD BANK ATM")
#     print("============================")
#     print("1. Check Balance")
#     print("2. Deposit Money")
#     print("3. Withdraw Money")
#     print("4. Exit")
#     print("===========================")


#     choice = input (" Choose an option(1-4):")

#     if choice == "1":
#         print (f"\n your Current Balance is: N{balance:.2f}")

#     elif choice =="2" :
#         amount = float(input("\nEnter amount to deposit: N"))
#         if amount > 0:
#             balance += amount
#             print (f" N{amount:.2f}deposited successfully!")
#             print(f" your new balance is : N{balance:.2f}")
#         else:
#             print(" Invalid amount! Deposit must be greater than zero.")

#     elif choice == "3":
        
#         amount = float(input("\nEnter amount to withdraw: ₦"))
#         if amount <= 0:
#             print("❌ Invalid amount! Withdrawal must be greater than zero.")
#         elif amount > balance:
#             print(f"❌ Insufficient funds! You only have ₦{balance:.2f}")
#         else:
#             balance -= amount
#             print(f"✅ ₦{amount:.2f} withdrawn successfully!")
#             print(f"💰 Your remaining balance is: ₦{balance:.2f}")

#     elif choice == "4":
#         print("\n👋 Thank you for using Python ATM. Have a great day!")
#         break  # <--- Only break here to exit the loop!

#     else:
#         print("\n❌ Invalid choice! Please select an option between 1 and 4.")


# ==========================================
# 1. INITIAL SETUP
# ==========================================
balance = 5000.0  # Starting balance

# ==========================================
# 2. MAIN ATM LOOP
# ==========================================
while True:
    print("\n============================")
    print("    WELCOME TO PYTHON ATM   ")
    print("============================")
    print("1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Exit")
    print("============================")

    # Ask the user for their choice ONCE
    choice = input("Choose an option (1-4): ")

    # --------------------------------------
    # OPTION 1: CHECK BALANCE
    # --------------------------------------
    if choice == "1":
        print(f"\n💰 Your current balance is: ₦{balance:.2f}")

    # --------------------------------------
    # OPTION 2: DEPOSIT MONEY
    # --------------------------------------
    elif choice == "2":
        amount = float(input("\nEnter amount to deposit: ₦"))
        if amount > 0:
            balance += amount
            print(f"✅ ₦{amount:.2f} deposited successfully!")
            print(f"💰 Your new balance is: ₦{balance:.2f}")
        else:
            print("❌ Invalid amount! Deposit must be greater than zero.")

    # --------------------------------------
    # OPTION 3: WITHDRAW MONEY
    # --------------------------------------
    elif choice == "3":
        amount = float(input("\nEnter amount to withdraw: ₦"))
        if amount <= 0:
            print("❌ Invalid amount! Withdrawal must be greater than zero.")
        elif amount > balance:
            print(f"❌ Insufficient funds! You only have ₦{balance:.2f}")
        else:
            balance -= amount
            print(f"✅ ₦{amount:.2f} withdrawn successfully!")
            print(f"💰 Your remaining balance is: ₦{balance:.2f}")

    # --------------------------------------
    # OPTION 4: EXIT
    # --------------------------------------
    elif choice == "4":
        print("\n👋 Thank you for using Python ATM. Have a great day!")
        break  # <--- Only break here to exit the loop!

    # --------------------------------------
    # INVALID OPTION
    # --------------------------------------
    else:
        print("\n❌ Invalid choice! Please select an option between 1 and 4.")


    







   