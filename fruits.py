fruits = {
    "APPLE": 1000,
    "BANANA": 500,
    "MANGO": 1200
}

print("FRUIT PRICES:")
for fruit, price in fruits.items():
    print(f"{fruit}: {price} RWF PER 1 KG")

total_cost = 0
for price in fruits.values():
    total_cost += price * 2

print(f"TOTAL COST FOR 2 KG EACH FRUIT: {total_cost} RWF")