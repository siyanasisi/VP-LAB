def calculate_final_price(cart_items, user_status, promo_code):
    total = 0

    for item in cart_items:
        total += item["price"]

        loyalty_discount = {
            "regular": 0,
            "silver": 0.05, 
            "gold": 0.1
        }

        if user_status not in loyalty_discount:
            return 0, "invalid user status"

    loyalty_discount = total * loyalty_discount[user_status]

    promo_discounts = {
        "SAVE10": 0.1,
        "SAVE20": 0.2
    }

    subtotal = total - loyalty_discount

    if promo_code in promo_discounts:
        promo_discount = subtotal * promo_discounts[promo_code]
    else:
        promo_discount = 0

    final_price = subtotal - promo_discount

    invoice = {
        "total": round(total, 2),
        "loyalty_discount": round(loyalty_discount, 2),
        "promo_discount": round(promo_discount, 2),
        "final_price": round(final_price, 2)
    }

    return invoice

cart_items = [
    {"name": "item1", "price": 100},
    {"name": "item2", "price": 200},
    {"name": "item3", "price": 300}
]

result = calculate_final_price(cart_items, "gold", "SAVE10")
print(result)