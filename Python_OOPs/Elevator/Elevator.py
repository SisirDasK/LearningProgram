"""
    This module contains the properties of an elevator required for the simulation.
"""

class Elevator( object ):
    def __init__(self, noOfFloors):
        """
        noOfFloors: The number of floor in the building.
        curFloor: The floor at which the elevator is currently at.
        direction: The direction in which the elevator is currently going ('DOWN' or 'UP').
        """
        self.noOfFloors = noOfFloors
        self.curFloor = -1;
        self.direction = "UP"

    def move(self):
        """ This method moves the elevator one floor at a time. """

        print "Elevator moving"
        if self.direction == "UP" and self.curFloor < self.noOfFloors:
            self.curFloor = self.curFloor + 1
            if self.curFloor == self.noOfFloors:
                self.direction = "DOWN"
        elif self.direction == "DOWN" and self.curFloor > 0:
            self.curFloor = self.curFloor - 1
            if self.curFloor == 0:
                self.direction = "UP"
        return self.curFloor

    def customerEnter(self, customer):
        """ This method simulates the behavior of customer when he or she enters the elevator. """
        customer.in_elevator = True
        print "Customer " + str( customer.ID ) + " entered elevator"

    def customerExit(self, customer):
        """ This method simulates the behavior of customer when he or she exits the elevator. """
        customer.in_elevator = False
        customer.finished = True
        print "Customer " + str( customer.ID ) + " exit elevator"
