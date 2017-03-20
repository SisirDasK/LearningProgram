"""
    This module contains all the properties of a building required to simulate the elevator.
"""

from Elevator import Elevator
import sys

class Building( object ):
    def __init__( self, noOfFloors, customersList ):
        """
        noOfFloors: The number of floors in the building which is provided by the user.
        customersList: A list of customers which their source floor, destination floor and the direction they are going.
        elevator: An elevator object reference that is used to control the elevator.
        """
        self.noOfFloors = noOfFloors
        self.customersList = customersList
        self.elevator = Elevator( noOfFloors )

    def run( self ):
        """
        This method moves the elevator from floor to floor and picks up customers based on their direction and their source and destination floors.
        """
        curFloor = self.elevator.move()
        print "Elevator stopped at floor: %d" % curFloor

        for customer in self.customersList:
            if ( not customer.in_elevator ) and ( not customer.finished ):
                if customer.going == self.elevator.direction and curFloor == customer.cur_floor:
                    self.elevator.customerEnter( customer )
            elif customer.in_elevator and ( not customer.finished ):
                if curFloor == customer.dst_floor:
                    self.elevator.customerExit( customer )
        print

    def finish( self ):
        """
        This method ends the simulation.
        """
        print "All customers have reached their floors. Thank you!"
        sys.exit(0)
