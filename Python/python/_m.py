from classes_to_use import Bank
from My_Classes import my_mini_store as s
from My_Classes import my_mini_bank


#new thing enumarate()
user_bank=Bank()
user = s.PlushieStore(name="Hersy",financing=user_bank,bag={})
user.display_products_to_sell()
user.selecting_stuff()
user.pay_chart()