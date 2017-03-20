"""
    Elevator simulator
    Author: Sisir K
    Description: This program simulates the behaviour of an elevator.
"""

from Customer import Customer
from Elevator import Elevator
from Building import Building

while True:
    try:
        invalid = False
        noOfCustomers = int( input( "Please enter the number of customers: " ) )
        if noOfCustomers <= 0:
            invalid = True
            print "No. of customers should be a value greater than 0. Please try again."
        if not invalid:
            break
    except NameError:
        print "Please try again with a positive integer value."
    except SyntaxError:
        print "The simulator requires a positive integer value to continue. Please try again."

while True:
    try:
        invalid = False
        noOfFloors = int( input( "Please enter the number of floors: " ) )
        if noOfFloors <= 0:
            invalid = True
            print "No. of floors should be a value greater than 0. Please try again."
        if not invalid:
            break
    except NameError:
        print "Please try again with a positive integer value."
    except SyntaxError:
        print "The simulator requires a positive integer value to continue. Please try again."


customersList = []
i = 1

for i in range( 1, noOfCustomers + 1 ):
    customersList.append( Customer( i, noOfFloors ) )
    i = i + 1

building = Building( noOfFloors, customersList )

while True:
    i = 0
    for customerCheck in building.customersList:
        if customerCheck.finished:
            i = i + 1

    if i == len( building.customersList ):
        building.finish()
    else:
        building.run()
