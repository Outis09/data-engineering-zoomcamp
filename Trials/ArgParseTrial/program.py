import argparse
from datetime import datetime

# get current date
current_datetime = datetime.now()
# initialize argparse
parser = argparse.ArgumentParser(description="A program that does something")

# add positional arguments
parser.add_argument('product',help='Enter name of product',choices=['Rice','Oats','Sugar'])
parser.add_argument('quantity',type=int, help='Enter quantity')
parser.add_argument('unit_cost',type=float,help='Enter unit cost of product')
# add optional argument with a constant value
parser.add_argument('-a','--add_discount',metavar='N',
                    action='store_const',const=0.2,help='A discount of 20 percent is applied')
# add optional argument with default value
parser.add_argument('-d','--date',type=datetime, help='Enter date of purchase',
                    default=current_datetime)

# parse arguments
arguments = parser.parse_args()

# assign arguments to variable
product = arguments.product
quantity = arguments.quantity
unit_cost = arguments.unit_cost
discount = arguments.add_discount
purchase_date  = arguments.date
# print arguments
# print(arguments)



if discount != None:
    cost_after_discount = (1 -discount) * (unit_cost * quantity)
    print(f'You ordered {quantity} of {product} at a unit cost of ${unit_cost} on {purchase_date}.')
    print('\n')
    print(f'After discount is applied, your total cost is ${cost_after_discount}')
else:
    cost_without_discount = unit_cost * quantity
    print(f'You ordered {quantity} of {product} at a unit cost of ${unit_cost}.')
    print('\n')
    print(f'Your total cost is {cost_without_discount}')

print('--------------------------------------------')
