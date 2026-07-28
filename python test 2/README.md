<div align="center">

# 📦 Inventory List Analyzer

### A simple yet powerful Python console app to manage and analyze inventory data

[![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=flat-square&logo=python&logoColor=white)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-green?style=flat-square)](#)
[![Status](https://img.shields.io/badge/Status-Completed-brightgreen?style=flat-square)](#)

</div>

---

## 📖 About The Project

**Inventory List Analyzer** is a Python-based console application that allows users to enter multiple inventory items along with their category and quantity. The program stores the data, performs various analyses, sorts the inventory by quantity, displays categories alphabetically, and generates a detailed inventory summary.

The application demonstrates the practical use of core Python data structures, loops, sorting algorithms, and user input handling — making it an excellent beginner-friendly project for learning fundamental programming concepts.

---

## ✨ Features

- ➕ Add multiple inventory items
- 📋 Store item names using a **List**
- 🗂️ Store item categories using a **Set**
- 🔢 Store quantities using a **List**
- 🔁 Allow continuous user input until the user chooses to stop
- 📊 Display key statistics:
  - Total Items
  - Total Quantity
  - Average Quantity
  - Highest Quantity
  - Lowest Quantity
- 🏷️ Display all unique categories
- ⬇️ Sort items according to quantity (Highest to Lowest)
- 🔤 Display categories in alphabetical order
- 💻 Interactive console interface
- 🌱 Beginner-friendly Python project

---

## 🧠 Python Concepts Used

| Concept | Description |
|---|---|
| Variables | Storing and managing user data |
| Lists | Storing item names and quantities |
| Sets | Storing unique item categories |
| Loops | Repeating input and processing tasks |
| Nested Loops | Comparing and sorting inventory data |
| Conditional Statements | Controlling program flow and logic |
| User Input | Capturing data interactively via console |
| Bubble Sort | Sorting inventory by quantity |
| Built-in Functions | `len()`, `sum()`, `max()`, `min()`, `sorted()` |
| String Formatting | Displaying clean, readable output |
| Data Processing | Analyzing and summarizing inventory data |

---

## 🛠️ Technologies Used

- 🐍 Python 3
- 💻 Visual Studio Code
- ⌨️ Command Prompt / Terminal

---

## ⚙️ Installation

Follow these steps to set up the project on your local machine:

1. **Install Python 3**
   Download and install Python 3 from the [official website](https://www.python.org/downloads/) if you haven't already.

2. **Clone the repository**
   ```bash
   git clone https://github.com/dhyeykakadiya71-dotcom/python-exam.git
   ```

3. **Navigate to the project folder**
   ```bash
   cd "python-exam/python test 2"
   ```

4. **Verify Python installation**
   ```bash
   python --version
   ```

No external libraries are required — the project runs using Python's standard library only.

---

## ▶️ How to Run

1. Open the project folder in **Visual Studio Code** or your preferred editor.
2. Open a terminal / command prompt in the project directory.
3. Run the script using the following command:

   ```bash
   python inventory_list_analyzer.py
   ```

4. Follow the on-screen prompts to enter item names, categories, and quantities.
5. Choose to stop entering data whenever you're ready to view the analysis.

---

## 📁 Project Structure

```
Inventory-List-Analyzer/
│── inventory_list_analyzer.py
│── output.png
│── README.md
```

---

## 🖥️ Sample Output

```
=== Inventory List Analyzer ===

Enter item name: Laptop
Enter category: Electronics
Enter quantity: 15
Add another item? (y/n): y

Enter item name: Chair
Enter category: Furniture
Enter quantity: 40
Add another item? (y/n): y

Enter item name: Mouse
Enter category: Electronics
Enter quantity: 60
Add another item? (y/n): n

=========== Inventory Summary ===========
Total Items       : 3
Total Quantity    : 115
Average Quantity  : 38.33
Highest Quantity  : 60
Lowest Quantity   : 15

Unique Categories : Electronics, Furniture

--- Items Sorted by Quantity (High to Low) ---
Mouse   - 60
Chair   - 40
Laptop  - 15

--- Categories (Alphabetical Order) ---
Electronics
Furniture
==========================================
```

---

## 📷 Output Screenshot

![Output](output.png)

---

## 👤 Author

**Dhyey Kakadiya**

🔗 GitHub: [dhyeykakadiya71-dotcom](https://github.com/dhyeykakadiya71-dotcom/python-exam/tree/main/python%20test%202)

---

<div align="center">

⭐ If you found this project useful, consider giving it a star on GitHub!

</div>
