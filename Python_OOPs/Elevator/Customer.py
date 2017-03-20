"""
    This module has all the properties of a customer.
"""

import random

class Customer( object ):
    def __init__( self, curCustomer, noOfFloors ):
        """
        ID: An identifier for each customer.
        in_elevator: Indicates whether the customer is inside the elevator (True) or outside the elevator (False)
        finished: Indicates if the customer has reached his or her destination floor.
        cur_floor: Tells the floor at which the customer is waiting for the elevator.
        dst_floor: Tells the destination floor of the customer.
        going: Tells the direction which the customer is going. (Possible values are 'DOWN' and 'UP')
        """

        self.ID = curCustomer
        self.in_elevator = False
        self.finished = False

        print "\n\n\n"

        while True:
            self.cur_floor = random.randint( 0, noOfFloors )
            self.dst_floor = random.randint( 0, noOfFloors )
            if self.cur_floor != self.dst_floor:
                if (self.dst_floor - self.cur_floor) > 0:
                    self.going = "UP"
                else:
                    self.going = "DOWN"
                print "Customer " + str( self.ID ) + ": \n\tFloor: " + str( self.cur_floor ) + "\n\tDestination: " + str( self.dst_floor ) + "\n\tGoing: " + self.going
                break

        print "\n\n\n"
