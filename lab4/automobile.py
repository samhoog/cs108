"""CS 108 Lab 4.0

This application prompts the user for an automobile service then
prints the cost.

@author: Sam Hoogewind (sth6)
@date: Fall, 2020
"""

# Create a dictionary of the available services and their costs
service_list = {
    'oil change': 35,
    'tire rotation': 19,
    'car wash': 7
}

# Prompt the user for a service and store it in a variable
service = input('service: ')

# If the picked service is in the dict, store and print its
# corrosponding price
if service in service_list:
    price = service_list[service]
    print('cost of ' + service + ': $' + str(price))

# If the picked service isn't in the dict, print an error
if service not in service_list:
    print('error: ' + service + ' is not recognized')
