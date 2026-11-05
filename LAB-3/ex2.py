def process_transaction(balance, transaction_type, amount, overdraft=0):
    if not isinstance(balance, (int, float)) or isinstance(balance, bool):
        return balance, "invalid balance"

    if not isinstance(amount, (int, float)) or isinstance(amount, bool):
        return balance, "invalid amount"

    if amount < 0:
        return balance, "amount must be positive"

    if not isinstance(overdraft, (int, float)) or isinstance(overdraft, bool) or overdraft < 0:
        return balance, "invalid overdraft"

    if transaction_type == "deposit":
        balance += amount

    elif transaction_type == "withdraw":
        fee = amount * 0.005 if amount > 1000 else 0
        total = amount + fee

        if total > balance + overdraft:
            return balance, "insufficient funds"

        balance -= total

    else:
        return balance, "invalid transaction type"

    return round(balance, 2), "transaction successful"


print(process_transaction(1000, "withdraw", 1500, 500))
print(process_transaction(1000, "withdraw", 500, 100))