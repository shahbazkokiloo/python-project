# 🛒 Smart Grocery Basket Optimizer

A **Python-based command-line grocery shopping application** that helps users build a grocery basket while staying within their budget.

The program allows users to add and remove grocery items, check their current spending, clear the basket, and receive suggestions for items they can still afford.

---

## ✨ Features

* 💰 Set a custom shopping budget
* 🛍️ View available grocery items and prices
* ➕ Add items to the basket
* 🚫 Prevent purchases that exceed the budget
* 🗑️ Remove items from the basket
* 👀 View the current basket
* 🧹 Clear the entire basket
* 📊 Calculate total spending automatically
* 💵 Display remaining budget
* 💡 Suggest affordable items based on the remaining budget
* ❌ Validate invalid budget input
* 🖥️ Simple command-line interface

---

## 📋 Available Items

| Item      | Price |
| --------- | ----: |
| Rice      |  ₹120 |
| Milk      |   ₹50 |
| Biscuits  |   ₹30 |
| Chocolate |   ₹80 |
| Bread     |   ₹40 |
| Eggs      |   ₹60 |

---

## 🛠️ Technologies Used

* **Python 3**
* Dictionaries
* Lists
* Functions
* Loops
* Conditional Statements
* Exception Handling
* String Formatting
* Docstrings
* User Input Handling

---

## 📂 Project Structure

```text
smart-grocery-basket/
│
├── grocery.py
└── README.md
```

---

## 🚀 How to Run

### 1. Clone the repository

```bash
git clone https://github.com/your-username/smart-grocery-basket.git
```

### 2. Open the project folder

```bash
cd smart-grocery-basket
```

### 3. Run the program

```bash
python grocery.py
```

---

## 🎮 Commands

While using the application, you can enter:

| Command       | Action                 |
| ------------- | ---------------------- |
| `rice`        | Add rice               |
| `milk`        | Add milk               |
| `biscuits`    | Add biscuits           |
| `chocolate`   | Add chocolate          |
| `bread`       | Add bread              |
| `eggs`        | Add eggs               |
| `show`        | Display current basket |
| `remove rice` | Remove rice            |
| `clear`       | Empty the basket       |
| `done`        | Finish shopping        |

---

## 💻 Example

```text
=============================================
SMART GROCERY BASKET OPTIMIZER
=============================================
Build a grocery basket while staying within your budget.
Default mode: Block unaffordable additions.

Enter your budget: 300

Available items:
  Rice       - ₹120
  Milk       - ₹50
  Biscuits   - ₹30
  Chocolate  - ₹80
  Bread      - ₹40
  Eggs       - ₹60

Enter item or command: rice
Rice added for ₹120.

Enter item or command: milk
Milk added for ₹50.

Enter item or command: chocolate
Chocolate added for ₹80.

Enter item or command: show

Current basket:
  - Rice (₹120)
  - Milk (₹50)
  - Chocolate (₹80)

Total: ₹250
Remaining: ₹50

Enter item or command: done

=============================================
FINAL BASKET SUMMARY
=============================================
Basket:
  - Rice (₹120)
  - Milk (₹50)
  - Chocolate (₹80)

Total cost: ₹250
Remaining budget: ₹50
Suggestion: You can add Biscuits, Bread
=============================================
```

---

## 🧠 How It Works

The application stores grocery items and their prices in a Python dictionary:

```python
items = {
    "rice": 120,
    "milk": 50,
    "biscuits": 30,
    "chocolate": 80,
    "bread": 40,
    "eggs": 60,
}
```

A list is used to store the user's selected items:

```python
basket = []
```

Before adding an item, the program calculates the current basket total and checks whether adding the new item would exceed the user's budget.

```python
current_total + item_price <= budget
```

This ensures that unaffordable items are blocked automatically.

---

## 🔧 Main Functions

### `show_catalog()`

Displays all available grocery items and their prices.

### `calculate_total()`

Calculates the total cost of the current basket.

### `can_add_item()`

Checks whether an item can be added without exceeding the budget.

### `suggest_items()`

Finds items that the user can still afford with the remaining budget.

### `add_item()`

Adds an item to the basket if it is available and affordable.

### `remove_item()`

Removes one occurrence of an item from the basket.

### `show_basket()`

Displays the current basket, total cost, and remaining budget.

### `print_summary()`

Displays the final shopping summary and affordable item suggestions.

### `get_budget()`

Validates the user's budget input and handles invalid values.

---

## 🎯 Learning Objectives

This project was created to practice and demonstrate fundamental Python programming concepts, including:

* Functions and modular programming
* Lists and dictionaries
* `for` and `while` loops
* `if/else` conditions
* Exception handling with `try/except`
* User input validation
* String manipulation
* Working with functions and parameters
* Building a menu-driven CLI application

---

## 🔮 Future Improvements

Possible future versions could include:

* 📦 Item quantities
* 🧾 Automatic receipt generation
* 💾 Save/load baskets using JSON
* 🗄️ Database integration
* 🏷️ Product categories
* 🔎 Search functionality
* 📊 Spending statistics
* 🖥️ GUI version
* 🌐 REST API using **FastAPI**
* 👤 User accounts and saved shopping lists

---

## 👨‍💻 Author

**Shahbaz Showkat**

BCA Hons — CASET College of Computer Science

### Connect With Me

* GitHub: [shahbazkokiloo](https://github.com/shahbazkokiloo)
* LinkedIn: [Shahbaaz Showkat](https://www.linkedin.com/in/shahbaaz-showkat-22547434/)
* Email: [shahbazbinshowkat@gmail.com](mailto:shahbazbinshowkat@gmail.com)

---

## ⭐ Support

If you found this project useful, consider giving the repository a ⭐ on GitHub!
