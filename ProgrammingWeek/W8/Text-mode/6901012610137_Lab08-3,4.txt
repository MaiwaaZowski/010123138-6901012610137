class Product():
  def __init__(self, name, price, quantity):
      self.name, self.price, self.quantity = name, price, quantity
  def __str__(self):
      return f"Name  :{self.name}\nPrice :{self.price}\nQnt.  :{self.quantity}"
  def show(self):
      print(self)
  def showTotal(self):
      total = self.price * self.quantity
      print(f"Total :{total}\n")

with open("product.txt","r") as file:
  line = file.readlines()
  count = len(line)
  products = [[] for _ in range(count)]

  for _ in range(count):
    part =  line[_].strip().split(",")
    name, price, quantity = part
    products[_] = [name, int(price), int(quantity)]

productObj = [Product(p[0], p[1], p[2]) for p in products]

for _ in productObj:
  _.show()
  _.showTotal()

#6901012610137
#lab08-3,4