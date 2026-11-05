
def calculate_monthly_budget(income, expenses_list):
    if income <= 0:
        return "Error: income must be positive"

    expenses_by_category = {}
    total_expenses = 0

    for expense in expenses_list:
        category = expense["category"]
        amount = expense["amount"]

        if amount < 0:
            return "Error: expense cannot be negative"

        if category in expenses_by_category:
            expenses_by_category[category] += amount
        else:
            expenses_by_category[category] = amount

        total_expenses += amount

    remaining = income - total_expenses

    report = {
        "income": round(income, 2),
        "expenses_by_category": {},
        "total_expenses": round(total_expenses, 2),
        "remaining": round(remaining, 2),
        "advice": ""
    }

    for category, amount in expenses_by_category.items():
        percentage = (amount / income) * 100
        report["expenses_by_category"][category] = {
            "amount": round(amount, 2),
            "percentage": round(percentage, 2)
        }

    if remaining > 0:
        report["advice"] = "You are within budget and have money left."
    elif remaining == 0:
        report["advice"] = "You have used your entire budget."
    else:
        report["advice"] = "You are over budget. Reduce your expenses."

    return report


income = 3000

expenses = [
    {"category": "Food", "amount": 500},
    {"category": "Rent", "amount": 1000},
    {"category": "Transport", "amount": 200},
    {"category": "Food", "amount": 300},
    {"category": "Entertainment", "amount": 150}
]

result = calculate_monthly_budget(income, expenses)

print(result)
