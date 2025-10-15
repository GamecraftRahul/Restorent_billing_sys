import customtkinter as ctk
from tkinter import messagebox
import mysql.connector
from datetime import datetime

# ------------------ DB CONFIG ------------------
DB_CONFIG = {
    "host": "localhost",
    "user": "root",
    "password": "RAHUL123",  # <<< CHANGE THIS
    "database": "restaurant_db"
}

# ------------------ MAIN APP ------------------
class RestaurantBillingApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("🍽️ Restaurant Billing System")
        self.geometry("1000x650")
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("green")

        self.menu_items = {}
        self.cart = []
        self.discount_value = 0
        self.create_ui()
        self.load_menu()

    def create_ui(self):
        # ---------- Header ----------
        ctk.CTkLabel(self, text="🍕 Restaurant Billing System 🍔", font=("Arial Rounded MT Bold", 26)).pack(pady=10)

        # ---------- Frames ----------
        main_frame = ctk.CTkFrame(self)
        main_frame.pack(fill="both", expand=True, padx=10, pady=10)

        left_frame = ctk.CTkFrame(main_frame, corner_radius=15)
        left_frame.pack(side="left", fill="both", expand=True, padx=10, pady=10)

        right_frame = ctk.CTkFrame(main_frame, corner_radius=15)
        right_frame.pack(side="right", fill="both", expand=True, padx=10, pady=10)

        # ---------- Left Frame (Product Entry) ----------
        ctk.CTkLabel(left_frame, text="Add Product", font=("Arial", 20)).pack(pady=10)

        self.product_entry = ctk.CTkEntry(left_frame, placeholder_text="Type product name", width=250)
        self.product_entry.pack(pady=5)
        self.product_entry.bind("<KeyRelease>", self.show_suggestions)

        self.suggestion_box = ctk.CTkTextbox(left_frame, width=250, height=100)
        self.suggestion_box.pack(pady=5)
        self.suggestion_box.bind("<Button-1>", self.select_suggestion)

        self.price_entry = ctk.CTkEntry(left_frame, placeholder_text="Price", width=250)
        self.price_entry.pack(pady=5)

        self.qty_entry = ctk.CTkEntry(left_frame, placeholder_text="Quantity", width=250)
        self.qty_entry.pack(pady=5)

        self.add_btn = ctk.CTkButton(left_frame, text="Add to Cart", command=self.add_to_cart)
        self.add_btn.pack(pady=10)

        # ---------- Discount ----------
        ctk.CTkLabel(left_frame, text="Discount (₹ or %)", font=("Arial", 16)).pack(pady=10)
        self.discount_entry = ctk.CTkEntry(left_frame, placeholder_text="e.g., 50 or 10%", width=250)
        self.discount_entry.pack(pady=5)
        self.discount_entry.bind("<KeyRelease>", lambda e: self.update_cart())

        # ---------- Right Frame (Cart & Bill) ----------
        ctk.CTkLabel(right_frame, text="🛒 Cart", font=("Arial", 20)).pack(pady=10)
        self.cart_box = ctk.CTkTextbox(right_frame, width=400, height=300)
        self.cart_box.pack(padx=10, pady=10)

        self.total_label = ctk.CTkLabel(right_frame, text="Total: ₹0.00", font=("Arial", 18))
        self.total_label.pack(pady=10)

        self.customer_entry = ctk.CTkEntry(right_frame, placeholder_text="Customer Name")
        self.customer_entry.pack(pady=5)

        ctk.CTkButton(right_frame, text="Save Bill", command=self.save_bill).pack(pady=8)
        ctk.CTkButton(right_frame, text="View Bills", command=self.view_bills).pack(pady=5)
        ctk.CTkButton(right_frame, text="Print Preview", command=self.print_preview).pack(pady=5)

    # ---------- DATABASE ----------
    def connect_db(self):
        return mysql.connector.connect(**DB_CONFIG)

    def load_menu(self):
        try:
            conn = self.connect_db()
            cur = conn.cursor()
            cur.execute("SELECT name, price FROM items")
            for name, price in cur.fetchall():
                self.menu_items[name.lower()] = float(price)
            conn.close()
        except Exception as e:
            messagebox.showerror("Error", str(e))

    # ---------- SEARCH & AUTO FILL ----------
    def show_suggestions(self, event):
        typed = self.product_entry.get().lower()
        self.suggestion_box.delete("1.0", "end")

        if not typed:
            return
        matches = [name for name in self.menu_items if typed in name]
        for m in matches[:8]:
            self.suggestion_box.insert("end", f"{m.title()}\n")

    def select_suggestion(self, event):
        try:
            line = self.suggestion_box.get("insert linestart", "insert lineend").strip()
            if not line:
                return
            self.product_entry.delete(0, "end")
            self.product_entry.insert(0, line)
            self.price_entry.delete(0, "end")
            self.price_entry.insert(0, str(self.menu_items[line.lower()]))
            self.suggestion_box.delete("1.0", "end")
        except Exception:
            pass

    # ---------- CART ----------
    def add_to_cart(self):
        name = self.product_entry.get().strip()
        if not name:
            messagebox.showinfo("Missing", "Enter product name.")
            return
        try:
            qty = int(self.qty_entry.get())
            price = float(self.price_entry.get())
        except ValueError:
            messagebox.showwarning("Invalid", "Enter valid price and quantity.")
            return
        total = qty * price
        self.cart.append((name, qty, price, total))
        self.update_cart()
        self.clear_product_fields()

    def clear_product_fields(self):
        self.product_entry.delete(0, "end")
        self.price_entry.delete(0, "end")
        self.qty_entry.delete(0, "end")

    def update_cart(self):
        self.cart_box.delete("1.0", "end")
        subtotal = 0
        for item in self.cart:
            name, qty, price, total = item
            subtotal += total
            self.cart_box.insert("end", f"{name} x{qty} = ₹{total:.2f}\n")

        discount_text = self.discount_entry.get().strip()
        discount = 0
        if discount_text:
            if discount_text.endswith("%"):
                percent = float(discount_text.strip("%"))
                discount = subtotal * (percent / 100)
            else:
                discount = float(discount_text)
        final_total = subtotal - discount
        self.total_label.configure(text=f"Total: ₹{final_total:.2f}")

    def save_bill(self):
        if not self.cart:
            messagebox.showwarning("Empty", "Cart is empty.")
            return

        name = self.customer_entry.get() or "Walk-in"
        subtotal = sum(x[3] for x in self.cart)

        discount_text = self.discount_entry.get().strip()
        discount = 0
        if discount_text:
            if discount_text.endswith("%"):
                discount = subtotal * (float(discount_text.strip('%')) / 100)
            else:
                discount = float(discount_text)

        total = subtotal - discount

        try:
            conn = self.connect_db()
            cur = conn.cursor()
            cur.execute("INSERT INTO bills (customer_name, total) VALUES (%s, %s)", (name, total))
            conn.commit()
            conn.close()
            messagebox.showinfo("Saved", f"Bill saved for {name} (₹{total:.2f})")

            # ✅ Clear all fields after saving
            self.cart.clear()
            self.customer_entry.delete(0, "end")
            self.discount_entry.delete(0, "end")
            self.update_cart()

        except Exception as e:
            messagebox.showerror("Error", str(e))

    def view_bills(self):
        try:
            conn = self.connect_db()
            cur = conn.cursor()
            cur.execute("SELECT bill_id, customer_name, total, date_time FROM bills ORDER BY bill_id DESC LIMIT 10")
            rows = cur.fetchall()
            conn.close()

            win = ctk.CTkToplevel(self)
            win.title("Past Bills")
            text = ctk.CTkTextbox(win, width=400, height=300)
            text.pack(padx=10, pady=10)
            for r in rows:
                text.insert("end", f"Bill #{r[0]} | {r[1]} | ₹{r[2]} | {r[3]}\n")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def print_preview(self):
        if not self.cart:
            messagebox.showinfo("Empty", "No items to print.")
            return
        win = ctk.CTkToplevel(self)
        win.title("Print Preview")
        txt = ctk.CTkTextbox(win, width=400, height=400)
        txt.pack(padx=10, pady=10)
        txt.insert("end", f"*** RESTAURANT BILL ***\nDate: {datetime.now()}\n")
        txt.insert("end", f"Customer: {self.customer_entry.get() or 'Walk-in'}\n\n")
        txt.insert("end", f"{'Item':20}{'Qty':>5}{'Price':>10}{'Total':>10}\n")
        txt.insert("end", "-" * 50 + "\n")
        subtotal = 0
        for i in self.cart:
            txt.insert("end", f"{i[0]:20}{i[1]:>5}{i[2]:>10.2f}{i[3]:>10.2f}\n")
            subtotal += i[3]

        discount_text = self.discount_entry.get().strip()
        discount = 0
        if discount_text:
            if discount_text.endswith("%"):
                discount = subtotal * (float(discount_text.strip('%')) / 100)
            else:
                discount = float(discount_text)

        total = subtotal - discount
        txt.insert("end", "-" * 50 + f"\nSubtotal = ₹{subtotal:.2f}\nDiscount = ₹{discount:.2f}\nTOTAL = ₹{total:.2f}")

# ------------------ RUN APP ------------------
if __name__ == "__main__":
    app = RestaurantBillingApp()
    app.mainloop()
