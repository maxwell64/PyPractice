#an exercise in class manipulation, creating classes for products and inventories, allowing a listing of all products,
#printing of total inventory value, and the searching for a product by name, returning the inventory ID

class Product:

  def __init__(self,ID,name,price,quantity):

    self.ID = ID
    self.name = name
    self.price = price
    self.quantity = quantity

class Inventory:
  
  def __init__(self):

    self.inv_list = []

  def addProd(self,prod):

    self.inv_list.append(prod)

  def value(self):

    total_val = 0

    for i in self.inv_list:

      total_val += i.price * i.quantity

    print('The total value of the inventory is %s'% total_val)
  
  def invList(self):

    for i in self.inv_list:

      print(i.name)
  
  def invSearch(self,arg):

    for i in self.inv_list:

      if i.name == arg:

        print('The ID number of the product is %s'% i.ID)
        return
    
    print('This product is currently unavailable')
    

prod1 = Product(0,'cheese',5.50,40)
prod2 = Product(1,'fish',12,10)
prod3 = Product(2,'cat',2,5)

stock = Inventory()

stock.addProd(prod1)
stock.addProd(prod2)
stock.addProd(prod3)

stock.invList()
stock.value()
stock.invSearch('dog')
