#!/usr/bin/env python3

class CashRegister:
  def __init__(self, cash_register=None, discount=0):
    self.cash_register = cash_register
    self.discount = discount
    
  @property
  def cash_register(self):
    return self._cash_register
  
  @cash_register.setter
  def cash_register(self, cash_register):
    self._cash_register = cash_register
    
  @property
  def discount(self):
    return self._discount
  
  @discount.setter
  def discount(self, discount):
    self._discount = discount
    
