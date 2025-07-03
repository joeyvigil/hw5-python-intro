def  calculate_budget():
    income = float(input("Enter your monthly income: $"))
    rent = float(input("Enter rent expense: $"))
    food = float(input("Enter food expense: $"))
    entertainment = float(input("Enter entertainment expense: $"))
    left=income-food-rent-entertainment
    print("\n=== BUDGET SUMMARY ===")
    print(f"Monthly Income: ${income}")
    print(f"Total Expenses: ${food+rent+entertainment}")
    print(f"Remaining Money: ${left}\n")
    if(left < 0):
        print("You're overspending! Cut back on expenses.")
    if(left < 100):
        print("Your budget is tight. Be careful with spending.")
    if(left >= 100):
        print("Great job! You have money left over.")
    

calculate_budget()