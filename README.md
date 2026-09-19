# 🏧 Simple Python ATM Simulator

A beginner-friendly console-based ATM (Automated Teller Machine) system built in Python. The application allows users to check their current balance, deposit funds, withdraw money with real-time balance validation, and exit cleanly through an interactive loop.

---

## 🚀 Features

- **Interactive Menu:** A clean terminal-based interface using a continuous loop.
- **Check Balance:** Instantly display your current account balance.
- **Deposit Funds:** Add money to your account with zero/negative value prevention.
- **Withdraw Funds:** Withdraw money with insufficient fund checks and negative input validation.
- **Input Validation:** Gracefully handles invalid menu selections without crashing.

---

## 🧠 Concepts Learned & Applied

- **`while True` Loops:** Keeping the program alive until the user explicitly chooses to exit.
- **Control Flow (`if / elif / else`):** Routing menu decisions dynamically.
- **Input Validation:** Checking numerical constraints before performing balance updates.
- **String Formatting (f-strings):** Formatting floating-point numbers to two decimal places (`₦{balance:.2f}`).
- **State Management:** Tracking and mutating the `balance` variable across multiple transactions.

---

## 🖥️ Sample Terminal Session

```text
============================
    WELCOME TO PYTHON ATM   
============================
1. Check Balance
2. Deposit Money
3. Withdraw Money
4. Exit
============================
Choose an option (1-4): 1

💰 Your current balance is: ₦5000.00

============================
    WELCOME TO PYTHON ATM   
============================
1. Check Balance
2. Deposit Money
3. Withdraw Money
4. Exit
============================
Choose an option (1-4): 2

Enter amount to deposit: ₦2500
✅ ₦2500.00 deposited successfully!
💰 Your new balance is: ₦7500.00

============================
    WELCOME TO PYTHON ATM   
============================
1. Check Balance
2. Deposit Money
3. Withdraw Money
4. Exit
============================
Choose an option (1-4): 3

Enter amount to withdraw: ₦10000
❌ Insufficient funds! You only have ₦7500.00

============================
    WELCOME TO PYTHON ATM   
============================
1. Check Balance
2. Deposit Money
3. Withdraw Money
4. Exit
============================
Choose an option (1-4): 4

👋 Thank you for using Python ATM. Have a great day!
