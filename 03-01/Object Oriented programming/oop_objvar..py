
class Robot:
    """Represents a robot, with a name."""

    # A class variable, counting the number of robots
    population = 0

    def __init__(self,name):
        """initializes the data."""
        self.name =name
        print("(initializing {}".format(self.name))


        # when this person is created, the robot
        # adds to the population
        Robot.population += 1
        
    def die(self):
            """i am dying."""
            print("{} is being detroyed!".format(self.name))

            Robot.population-= 1

            if Robot.population == 0:
                print("{} was the last one,".format(self.name))
            else:
                print("there are still {:d} robots working.".format(
                    Robot.population))
        
    def say_hi(self):
            """Greeting by the robot.
            
            yeah, they can do that."""
            print("Greeting, my masters call me {}.".format(self.name))

    @classmethod
    def how_many(cls):
            """prints the current population."""
            print("we have {:d} robots.".format(cls.population))

droid1 = Robot("R2-D2")
droid1.say_hi()
Robot.how_many()

droid2 = Robot ("C-3PO")
droid2.say_hi()
Robot.how_many()

print("\nRobots can do same work hare.\n")

print("Robots have finished their work.so let's destroy them.")
droid1.die()
droid2.die()

Robot.how_many()
