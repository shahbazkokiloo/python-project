items = {
    "rice": 120,
    "milk": 50,
    "biscuits": 30,
    "chocolate": 80,
    "bread": 40,
    "eggs": 60,
}


def show_catalog(items):
    """Display all available grocery items and their prices."""
    print("\nAvailable items:")
    for item, price in items.items():
        print(f"  {item.title():10} - ₹{price}")


def calculate_total(basket, items):
    """Return the total cost of all items in the basket."""
    total = 0

    for item in basket:
        total += items[item]

    return total


def can_add_item(budget, basket, items, item):
    """Check whether an item can be added without exceeding the budget."""
    current_total = calculate_total(basket, items)
    item_price = items[item]

    return current_total + item_price <= budget


def suggest_items(remaining, items, basket):
    """
    Return items that are not already in the basket
    and whose price fits within the remaining budget.
    """
    suggestions = []

    for item, price in items.items():
        if item not in basket and price <= remaining:
            suggestions.append(item)

    return suggestions


def print_summary(budget, basket, items):
    """Print the final basket, total, remaining budget and suggestions."""
    total = calculate_total(basket, items)
    remaining = budget - total

    print("\n" + "=" * 45)
    print("FINAL BASKET SUMMARY")
    print("=" * 45)

    if basket:
        print("Basket:")
        for item in basket:
            print(f"  - {item.title()} (₹{items[item]})")
    else:
        print("Basket: Empty")

    print(f"\nTotal cost: ₹{total}")
    print(f"Remaining budget: ₹{remaining}")

    if remaining < 0:
        print(f"Over budget by ₹{abs(remaining)}")
    else:
        suggestions = suggest_items(remaining, items, basket)

        if suggestions:
            readable = ", ".join(item.title() for item in suggestions)
            print(f"Suggestion: You can add {readable}")
        else:
            print("Suggestion: No items fit your remaining budget.")

    print("=" * 45)


def get_budget():
    """Read and validate a positive numeric budget."""
    while True:
        user_input = input("Enter your budget: ").strip()

        try:
            budget = float(user_input)

            if budget > 0:
                return budget

            print("Budget must be greater than 0.")

        except ValueError:
            print("Invalid budget. Please enter a number.")


def add_item(budget, basket, items, item):
    """
    Try to add an item to the basket.
    Returns True if added, otherwise False.
    """
    if item not in items:
        print("Item not found.")
        return False

    if can_add_item(budget, basket, items, item):
        basket.append(item)
        print(f"{item.title()} added for ₹{items[item]}.")
        return True

    remaining = budget - calculate_total(basket, items)
    print(f"Cannot add. Only ₹{remaining:.2f} left.")
    return False


def show_basket(basket, items, budget):
    """Display the current basket, total and remaining budget."""
    total = calculate_total(basket, items)
    remaining = budget - total

    print("\nCurrent basket:")
    if not basket:
        print("  Empty")
    else:
        for item in basket:
            print(f"  - {item.title()} (₹{items[item]})")

    print(f"Total: ₹{total}")
    print(f"Remaining: ₹{remaining}")


def remove_item(basket, item):
    """Remove one occurrence of an item from the basket."""
    if item in basket:
        basket.remove(item)
        print(f"{item.title()} removed from basket.")
        return True

    print("That item is not in your basket.")
    return False


def main():
    """Run the Smart Grocery Basket Optimizer."""
    print("=" * 45)
    print("SMART GROCERY BASKET OPTIMIZER")
    print("=" * 45)
    print("Build a grocery basket while staying within your budget.")
    print("Default mode: Block unaffordable additions.")
    budget = get_budget()
    basket = []

    show_catalog(items)

    print("\nCommands:")
    print("  item name     -> add an item")
    print("  done          -> finish shopping")
    print("  show          -> show current basket")
    print("  remove item   -> remove an item")
    print("  clear         -> empty the basket")

    while True:
        command = input("\nEnter item or command: ").strip().lower()

        # Ignore empty input
        if not command:
            print("Please enter an item or command.")
            continue

        # Finish shopping
        if command == "done":
            break

        # Show basket
        if command == "show":
            show_basket(basket, items, budget)
            continue

        # Clear basket
        if command == "clear":
            basket.clear()
            print("Basket cleared.")
            continue

        # Remove item
        if command.startswith("remove "):
            item = command[7:].strip()

            if item in items:
                remove_item(basket, item)
            else:
                print("Item not found.")

            continue

        # Add item
        add_item(budget, basket, items, command)

    print_summary(budget, basket, items)


if __name__ == "__main__":
    main()