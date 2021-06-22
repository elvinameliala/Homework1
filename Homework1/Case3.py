class Lift:
    def __init__ (self, CurrentFloor=2, MaxPeople=6, MaxFloor=4):
        self.CurrentFloor = CurrentFloor
        self.MaxPeople    = MaxPeople
        self.MaxFloor     = MaxFloor
             
    def Move (self, people):
        if (people < self.MaxPeople):
            print ("The door closed")
        else:
            print ("The door cannot be closed")
       
    def Elev (self, destination):
        if (destination <= self.MaxFloor):
            self.CurrentFloor = destination
            print ("You reach {} floor" .format(self.CurrentFloor))
        else:
            print ("can't move")

PanggilLift= Lift()
people = int(input("...number of people..."))
PanggilLift.Move(people)
destination = int(input("your destination floor"))
PanggilLift.Elev(destination)