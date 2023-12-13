#!/usr/bin/env python3

class CashRegister:
  #constructor 
  def __init__(self, discount=0):
    self.discount = discount
    self.total = 0
    self.items=[]
    self.last_transaction=[]

  def add_item(self, title, price, quantity=1):
    self.total += price * quantity
    for i in range(quantity):
      self.items.append(title)
    self.last_transaction.append({'title': title, 'price': price, 'quantity': quantity}),

  def apply_discount(self):
    if self.discount>0:
      self.total = int(((100-self.discount)/100)*self.total)
      print(f"After the discount, the total comes to ${self.total}.")

    else:
      print("There is no discount to apply.")

  def void_last_transaction(self):
    self.total -= self.last_transaction[-1]["price"]*self.last_transaction[-1]["quantity"]
