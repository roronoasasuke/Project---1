import heapq
import math

class Driver:
    def __init__(self, name, x, y, rating):
        self.name = name
        self.x = x
        self.y = y
        self.rating = rating

    def dist(self, rx, ry):
        return math.hypot(self.x - rx, self.y - ry)

class Rider:
    def __init__(self, name, x, y):
        self.name = name
        self.x = x
        self.y = y

class Dispatch:
    def __init__(self):
        self.drivers = []
        self.history = []

    def add_driver(self, driver):
        self.drivers.append(driver)

    def request_ride(self, rider):
        pq = []
        for d in self.drivers:
            heapq.heappush(pq, (d.dist(rider.x, rider.y), -d.rating, d))
        if pq:
            dist, neg_rating, driver = heapq.heappop(pq)
            self.history.append((rider.name, driver.name, dist, -neg_rating))
            self.drivers.remove(driver)
            return driver, dist, -neg_rating
        return None, None, None

    def ride_history(self):
        return self.history

def print_menu():
    print("\n🚗 Ride-Sharing Dispatch Simulator 🚦")
    print("1️⃣  Add Driver")
    print("2️⃣  Request Ride")
    print("3️⃣  Show Available Drivers")
    print("4️⃣  Show Ride History")
    print("5️⃣  Exit")

def main():
    dispatch = Dispatch()
    while True:
        print_menu()
        choice = input("Choose an option: ")
        if choice == "1":
            print("👨‍✈️ Add Driver")
            name = input("Driver name: ")
            try:
                x = float(input("Driver location X: "))
                y = float(input("Driver location Y: "))
                rating = float(input("Driver rating (1-5): "))
            except ValueError:
                print("❌ Invalid input. Try again.")
                continue
            dispatch.add_driver(Driver(name, x, y, rating))
            print(f"✅ Driver {name} added!")
        elif choice == "2":
            print("🧑‍🦰 Request Ride")
            name = input("Rider name: ")
            try:
                x = float(input("Rider location X: "))
                y = float(input("Rider location Y: "))
            except ValueError:
                print("❌ Invalid input. Try again.")
                continue
            rider = Rider(name, x, y)
            driver, dist, rating = dispatch.request_ride(rider)
            if driver:
                print(f"🚕 {driver.name} (⭐ {rating}) assigned to {name}! Distance: {dist:.2f}")
            else:
                print("😔 No drivers available.")
        elif choice == "3":
            print("🚙 Available Drivers:")
            if not dispatch.drivers:
                print("  (none)")
            for d in dispatch.drivers:
                print(f"  {d.name} at ({d.x}, {d.y}) ⭐ {d.rating}")
        elif choice == "4":
            print("📜 Ride History:")
            if not dispatch.history:
                print("  (none)")
            for i, (rider, driver, dist, rating) in enumerate(dispatch.history, 1):
                print(f"  {i}. {rider} 🚖 {driver} | Distance: {dist:.2f} | ⭐ {rating}")
        elif choice == "5":
            print("👋 Goodbye!")
            break
        else:
            print("❓ Invalid option. Try again.")

if __name__ == "__main__":
    main()