class Vehicle:
    def __init__(self, license_plate, brand, model, year, daily_rate):
        self.license_plate = license_plate
        self.brand = brand
        self.model = model
        self.year = year
        self.daily_rate = daily_rate
 
    def show_info(self):
        print("ป้ายทะเบียน:", self.license_plate)
        print("ยี่ห้อ:", self.brand)
        print("รุ่น:", self.model)
        print("ปี:", self.year)
        print("ค่าเช่ารายวัน:", self.daily_rate)
 
    def calculate_rental_cost(self, days):
        return self.daily_rate * days
 
 
class Car(Vehicle):
    def __init__(self, license_plate, brand, model, year, daily_rate, seats):
        super().__init__(license_plate, brand, model, year, daily_rate)
        self.seats = seats
 
    def show_info(self):
        super().show_info()
        print("จำนวนที่นั่ง:", self.seats)
 
    def calculate_rental_cost(self, days):
        # โปรโมชั่น: เช่า 5 วัน แถมฟรี 2 วัน (ได้ใช้ 7 วัน จ่ายแค่ 5 วัน)
        if days == 5:
            print("โปรโมชั่น! เช่า 5 วัน แถมฟรี 2 วัน (รวม 7 วัน)")
        return super().calculate_rental_cost(days)   # จ่ายตามจำนวนวันที่เช่าจริง
 
 
class Truck(Vehicle):
    def __init__(self, license_plate, brand, model, year, daily_rate, payload):
        super().__init__(license_plate, brand, model, year, daily_rate)
        self.payload = payload
 
    def show_info(self):
        super().show_info()
        print("น้ำหนักบรรทุก:", self.payload, "kg")
    # Truck ไม่มีโปรโมชั่น ใช้ calculate_rental_cost ของคลาสแม่

c = Car("กก 1234", "Toyota", "Yaris", 2022, 1000, 5)
t = Truck("ขข 5678", "Isuzu", "D-Max", 2021, 1500, 1000)
c.show_info()
print("ค่าเช่า 5 วัน:", c.calculate_rental_cost(5),"\n")
t.show_info()
print("ค่าเช่า 5 วัน:", t.calculate_rental_cost(5))

#6901012610137
#lab09-2