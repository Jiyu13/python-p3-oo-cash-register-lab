#!/usr/bin/env python3

class CashRegister:
  
  
  def __init__(self, discount=0, total=0):
    self.discount = discount  # optional arg
    self.total = total        # instance variable
    self.items = []
    self.transactions = []
    

  def add_item(self, title, price, quantity=1):

    self.total += price * quantity
    self.transactions.append(dict(title=title, price=price, quantity=quantity))

    if quantity != 0:
      if quantity == 1:
        self.items.append(title)
      else:
        times = quantity
        while times > 0:
          self.items.append(title)
          times -= 1
    return self.total

  
  def apply_discount(self, title="", price=0):
    if self.discount != 0:
      self.total = self.add_item(title, price) * (1 - 1 * self.discount / 100)
      print(f"After the discount, the total comes to ${int(self.total)}.")
    else:
      print("There is no discount to apply.")
    

  def items_list(self):
    return self.items


  def void_last_transaction(self):
    last_transactions_sum = self.transactions[-1]["price"] * self.transactions[-1]["quantity"]
    self.total = self.total - last_transactions_sum
    return self.total