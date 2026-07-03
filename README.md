# 🍽️ Restaurant Billing System

A modern **Restaurant Billing System** developed using **Python**, **CustomTkinter**, and **MySQL**. The application provides a clean graphical interface for creating restaurant bills, managing customer orders, applying discounts, and storing billing records in a MySQL database.

This project was built as a learning project to demonstrate Python GUI development, database connectivity, and billing system automation.

---

## 📖 Overview

The Restaurant Billing System simplifies the billing process by allowing restaurant staff to quickly add menu items, calculate totals, apply discounts, and save customer bills.

The application features a modern dark-themed interface built with **CustomTkinter**, making it more attractive and user-friendly than traditional Tkinter applications.

---

# ✨ Features

- 🍕 Modern CustomTkinter GUI
- 🛒 Add food items to cart
- 🔍 Product auto-suggestion while typing
- ➕ Specify quantity for each item
- 💰 Automatic bill calculation
- 🏷️ Apply discounts (Fixed Amount or Percentage)
- 👤 Customer name entry
- 💾 Save bills to MySQL database
- 📄 Print Preview
- 📚 View previous bills
- 🗄️ Dynamic menu loading from database

---

# 🛠️ Technologies Used

- Python 3
- CustomTkinter
- MySQL
- mysql-connector-python

---

# 📂 Project Structure

```
Restorent_billing_sys/
│
├── restorent_billing_sys.py      # Main Application
├── restorent_database.sql        # MySQL Database
├── README.md                     # Project Documentation
```

---

# 🗄️ Database

The project uses a MySQL database named:

```
restaurant_db
```

The menu items and billing records are stored in the database.

Import the SQL file before running the application.

---

# ⚙️ Installation

## 1. Clone the Repository

```bash
git clone https://github.com/your-username/restaurant-billing-system.git
```

---

## 2. Open the Project Folder

```bash
cd restaurant-billing-system
```

---

## 3. Install Required Libraries

```bash
pip install customtkinter
pip install mysql-connector-python
```

---

## 4. Import the Database

Open MySQL Workbench (or any MySQL client) and import:

```
restorent_database.sql
```

---

## 5. Configure Database Credentials

Open

```
restorent_billing_sys.py
```

Update the following configuration:

```python
DB_CONFIG = {
    "host": "localhost",
    "user": "your_username",
    "password": "your_password",
    "database": "restaurant_db"
}
```

---

## 6. Run the Application

```bash
python restorent_billing_sys.py
```

---

# 🖥️ Application Workflow

1. Load menu items from the database.
2. Search food items using auto-suggestions.
3. Enter quantity.
4. Add products to the cart.
5. Apply discount (Amount or Percentage).
6. Enter customer name.
7. Save the bill.
8. View previous bills.
9. Generate print preview.

---

# 📋 Main Features

### Product Management

- Dynamic menu loading
- Product search
- Auto-complete suggestions

### Billing

- Add multiple products
- Quantity management
- Automatic subtotal calculation
- Discount calculation
- Final amount calculation

### Customer Management

- Customer Name
- Bill History

### Database

- Store menu items
- Save billing records
- Retrieve previous bills

---

# 📚 Learning Objectives

This project demonstrates:

- Python GUI Development
- CustomTkinter Widgets
- Object-Oriented Programming
- MySQL Database Connectivity
- CRUD Operations
- Billing System Logic
- Event Handling
- Search & Auto-complete Implementation

---

# 🚀 Future Improvements

- 🔐 User Login & Authentication
- 🧾 PDF Bill Generation
- 🖨️ Direct Thermal Printer Support
- 📊 Sales Dashboard
- 📅 Daily & Monthly Reports
- 📦 Inventory Management
- 💳 Online Payment Integration
- 📱 QR Code Billing
- 🌐 Multi-user Support
- ☁️ Cloud Database Integration

---

# 📸 Screenshots

You can add screenshots here after uploading images.

```
Home Screen

Billing Window

Saved Bills

Print Preview
```

---

# 🤝 Contributing

Contributions are welcome.

1. Fork the repository
2. Create a new branch

```bash
git checkout -b feature-name
```

3. Commit your changes

```bash
git commit -m "Added new feature"
```

4. Push the branch

```bash
git push origin feature-name
```

5. Open a Pull Request

---

# 📄 License

This project is developed for educational and learning purposes.

You are free to use, modify, and improve this project for personal or academic use.

---

# 👨‍💻 Author

**Rahul Kulkarni**

GitHub: https://github.com/GamecraftRahul

---

## ⭐ Support

If you found this project helpful:

- ⭐ Star the repository
- 🍴 Fork the project
- 📢 Share it with others

---

## 💡 Project Highlights

✔ Modern CustomTkinter Interface

✔ MySQL Database Integration

✔ Auto Product Search

✔ Discount Calculation

✔ Customer Billing

✔ Bill History

✔ Print Preview

✔ Beginner-Friendly Code Structure

✔ Ideal Python Database Project

---

**Made with ❤️ using Python, CustomTkinter, and MySQL**
