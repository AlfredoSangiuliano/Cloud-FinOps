
from packages.get_products import *

ans=True
menu = """
    1.Show existing products
    2.Show expenses
    3.Show Spot or Ondemand EC2 expenses 
    4.Delete products (WIP)

    Enter to quit
"""

while ans:
    print(menu)
    ans=input("Select an option?: ")
    if ans=="1": 
        report()
    elif ans=="2":
      print("\n Option 2") 
    elif ans=="3":
      print("\n Option 3") 
    elif ans=="4":
      print("\n Option 4") 
    elif ans !="":
      print("\n Not Valid Choice Try again") 