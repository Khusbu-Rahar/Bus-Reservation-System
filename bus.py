import tkinter as tk
from tkinter import messagebox

# Predefined user credentials
users = {
    "user1": "pass1",
    "user2": "pass2",
    "user3": "pass3",
    "user4": "pass4",
    "user5": "pass5"
}

# Bus data
buses = {
    101: {"source": "City A", "destination": "City B", "totalSeats": 50, "availableSeats": 50, "fare": 500.0},
    102: {"source": "City C", "destination": "City D", "totalSeats": 40, "availableSeats": 40, "fare": 400.0},
    103: {"source": "City E", "destination": "City F", "totalSeats": 30, "availableSeats": 30, "fare": 300.0},
}


class BusReservationApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Bus Reservation System")
        self.logged_in_user = None
        self.login_screen()

    def login_screen(self):
        self.clear_window()

        tk.Label(self.root, text="Login", font=("Arial", 16)).pack(pady=10)
        tk.Label(self.root, text="Username").pack()
        self.username_entry = tk.Entry(self.root)
        self.username_entry.pack()
        tk.Label(self.root, text="Password").pack()
        self.password_entry = tk.Entry(self.root, show="*")
        self.password_entry.pack()

        tk.Button(self.root, text="Login", command=self.login).pack(pady=10)

    def main_menu(self):
        self.clear_window()
        tk.Label(self.root, text=f"Welcome, {self.logged_in_user}", font=("Arial", 14)).pack(pady=10)

        tk.Button(self.root, text="Book Ticket", width=20, command=self.book_ticket_screen).pack(pady=5)
        tk.Button(self.root, text="Cancel Ticket", width=20, command=self.cancel_ticket_screen).pack(pady=5)
        tk.Button(self.root, text="Check Bus Status", width=20, command=self.check_status_screen).pack(pady=5)
        tk.Button(self.root, text="Logout", width=20, command=self.logout).pack(pady=5)

    def book_ticket_screen(self):
        self.clear_window()
        tk.Label(self.root, text="Book Ticket", font=("Arial", 14)).pack(pady=10)

        tk.Label(self.root, text="Bus Number").pack()
        self.bus_number_entry = tk.Entry(self.root)
        self.bus_number_entry.pack()

        tk.Label(self.root, text="Number of Seats").pack()
        self.seats_entry = tk.Entry(self.root)
        self.seats_entry.pack()

        tk.Button(self.root, text="Book", command=self.book_ticket).pack(pady=10)
        tk.Button(self.root, text="Back", command=self.main_menu).pack()

    def cancel_ticket_screen(self):
        self.clear_window()
        tk.Label(self.root, text="Cancel Ticket", font=("Arial", 14)).pack(pady=10)

        tk.Label(self.root, text="Bus Number").pack()
        self.cancel_bus_number_entry = tk.Entry(self.root)
        self.cancel_bus_number_entry.pack()

        tk.Label(self.root, text="Seats to Cancel").pack()
        self.cancel_seats_entry = tk.Entry(self.root)
        self.cancel_seats_entry.pack()

        tk.Button(self.root, text="Cancel", command=self.cancel_ticket).pack(pady=10)
        tk.Button(self.root, text="Back", command=self.main_menu).pack()

    def check_status_screen(self):
        self.clear_window()
        tk.Label(self.root, text="Check Bus Status", font=("Arial", 14)).pack(pady=10)

        tk.Label(self.root, text="Bus Number").pack()
        self.status_bus_number_entry = tk.Entry(self.root)
        self.status_bus_number_entry.pack()

        tk.Button(self.root, text="Check", command=self.check_bus_status).pack(pady=10)
        tk.Button(self.root, text="Back", command=self.main_menu).pack()

    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        if username in users and users[username] == password:
            self.logged_in_user = username
            messagebox.showinfo("Login", "Login successful!")
            self.main_menu()
        else:
            messagebox.showerror("Login", "Invalid username or password.")

    def logout(self):
        self.logged_in_user = None
        self.login_screen()

    def book_ticket(self):
        try:
            bus_number = int(self.bus_number_entry.get())
            seats = int(self.seats_entry.get())

            if bus_number not in buses:
                messagebox.showerror("Error", "Bus not found.")
                return

            bus = buses[bus_number]

            if bus["availableSeats"] < seats:
                messagebox.showwarning("Warning", f"Only {bus['availableSeats']} seats are available.")
            else:
                bus["availableSeats"] -= seats
                messagebox.showinfo("Success", f"{seats} seat(s) booked on Bus {bus_number}.")
                self.main_menu()
        except ValueError:
            messagebox.showerror("Error", "Invalid input.")

    def cancel_ticket(self):
        try:
            bus_number = int(self.cancel_bus_number_entry.get())
            seats = int(self.cancel_seats_entry.get())

            if bus_number not in buses:
                messagebox.showerror("Error", "Bus not found.")
                return

            bus = buses[bus_number]
            booked_seats = bus["totalSeats"] - bus["availableSeats"]

            if seats > booked_seats:
                messagebox.showwarning("Warning", "Cannot cancel more seats than booked.")
            else:
                bus["availableSeats"] += seats
                messagebox.showinfo("Success", f"{seats} seat(s) cancelled on Bus {bus_number}.")
                self.main_menu()
        except ValueError:
            messagebox.showerror("Error", "Invalid input.")

    def check_bus_status(self):
        try:
            bus_number = int(self.status_bus_number_entry.get())

            if bus_number not in buses:
                messagebox.showerror("Error", "Bus not found.")
                return

            bus = buses[bus_number]
            status = (
                f"Bus Number: {bus_number}\n"
                f"Source: {bus['source']}\n"
                f"Destination: {bus['destination']}\n"
                f"Total Seats: {bus['totalSeats']}\n"
                f"Available Seats: {bus['availableSeats']}\n"
                f"Fare: {bus['fare']}"
            )
            messagebox.showinfo("Bus Status", status)
        except ValueError:
            messagebox.showerror("Error", "Invalid input.")

    def clear_window(self):
        for widget in self.root.winfo_children():
            widget.destroy()


# Run the GUI application
if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("350x400")
    app = BusReservationApp(root)
    root.mainloop()
