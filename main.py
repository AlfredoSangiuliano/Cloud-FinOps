
from packages.get_products import *
from packages.get_expenses import *
from packages.ec2_spot_count import *

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
        list_cost_generating_services() 
    elif ans=="3":
        list_ec2_costs()
    elif ans=="4":
      print("\n Option 4") 
    elif ans !="":
      print("\n Not Valid Choice Try again") 