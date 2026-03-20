"""
Assignment #3 
Task 2: Coding Task 

Submitted by: Mayur Bhawsar [C0958076]
"""
import json


# Original data
data = {
  "orders": [
    {
      "order_id": "O1001",
      "amount": 250,
      "status": "completed",
      "user": "u1"
    },
    {
      "order_id": "O1002",
      "amount": None,
      "status": "",
      "user": "u2"
    },
    {
      "order_id": "O1001",
      "amount": 250,
      "status": "completed",
      "user": "u1"
    },
    {
      "order_id": "O1003",
      "amount": "",
      "user": "u3"
    }
  ]
}


cleaned_orders = []
seen_order_ids = set()

# 1. clean data
for order in data["orders"]:
    if order["order_id"] in seen_order_ids:
        continue

    if order["amount"] is None or order["amount"] == "":
        order["amount"] = 0

    if "status" not in order or order["status"] is None or order["status"] == "":
        order["status"] = "pending"
    
    cleaned_orders.append(order)
    seen_order_ids.add(order["order_id"])


"""
--new list requirement:
{
"order_id": "...",
"amount": <number>,
"user": "..."
}
"""
# 2. build summary
summary_list = []

for order in cleaned_orders:
    summary_list.append({
        "order_id": order["order_id"],
        "amount": order["amount"],
        "user": order["user"]
    })
    
print("Cleaned Orders:")
print(json.dumps(cleaned_orders, indent=2))
print("\nSummary List:")
print(json.dumps(summary_list, indent=2))


